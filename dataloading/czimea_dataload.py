""" czimea_dataload.py

This module contains functions to be used in data loading to ODM2 Database.
For now, this module is limited to CZIMEA Database.
"""

import sys  # not used?
import json  # not used?

import os
import uuid
import datetime

import pandas as pd
from shapely.geometry import Point

from odm2api.ODMconnection import dbconnection
import odm2api.ODM2.models as odm2mod


__author__ = ['Landung Setiawan', 'Emilio Mayorga']


def get_df(dpth, fname, sheetname=0, skiprows=0):
    """
    Function made to get df from .csv or .xlsx
    """

    if fname.endswith('.csv'):
        df = pd.read_csv(os.path.join(dpth, fname), skiprows=skiprows)
    else:
        df = pd.read_excel(os.path.join(dpth, fname), sheetname=sheetname, skiprows=skiprows)
    return df


def get_dbsession(db_cred):
    """
    Function to get Database Connection Session

    db_cred = {
        'address': '127.0.0.1',
        'db': 'dbname',
        'user': 'dbuser',
        'password': 'password'
    }
    """

    session_factory = dbconnection.createConnection('postgresql', **db_cred)
    DBSession = session_factory.getSession()
    DBSession.expire_on_commit = False

    return DBSession


def create_samplingfeature(row, SF_set):
    """
    Function to create Sampling Features
    :row:    Row of dataframe
    :SF_set: Type of Sampling Features
    """

    SF = dict()

    # attr for samplingfeature
    SF['SamplingFeatureUUID'] = str(uuid.uuid1())
    SF['SamplingFeatureGeotypeCV'] = 'Point'
    point_shp = Point(row['lon'], row['lat'])
    SF['FeatureGeometryWKT'] = point_shp.wkt
    # SF['FeatureGeometry'] = point_shp.wkb_hex
    # Note: This doesn't set the SRID in FeatureGeometry. How to do that?!
    # ie, equivalent of PostGIS ST_SetSRID()
    # http://stackoverflow.com/questions/29500460/why-can-shapely-geos-parse-this-invalid-well-known-binary
    # http://git.net/ml/python-gis/2010-12/msg00016.html

    if SF_set == 'site':
        SF['SamplingFeatureTypeCV'] = 'Site'
        SF['SamplingFeatureCode'] = row['code']
        SF['SamplingFeatureName'] = row['name'] + ' Site'
        SF['SamplingFeatureDescription'] = '{0} Site ({1}) at {2} CZO'.format(
            row['name'], row['code'], row['czo'])

        # attr for sites
        SF['SiteTypeCV'] = 'Composite'
        SF['Latitude'] = row['lat']
        SF['Longitude'] = row['lon']
        SF['SpatialReferenceID'] = 1
        sf_object = odm2mod.Sites(**SF)
    elif SF_set == 'profile':
        SF['SamplingFeatureTypeCV'] = 'Profile'
        SF['SamplingFeatureCode'] = row['code'] + '-profile'
        SF['SamplingFeatureName'] = row['name'] + ' Soil Profile'
        SF['SamplingFeatureDescription'] = '{0} Soil Profile ({1}) at {2} CZO'.format(
            row['name'], row['code'], row['czo'])
        sf_object = odm2mod.SamplingFeatures(**SF)
    elif SF_set == 'coresection':
        SF['SamplingFeatureTypeCV'] = 'Specimen'
        depth_str = row['Depth'] + 'cm'
        SF['SamplingFeatureCode'] = row['code'] + '-profile-' + depth_str
        SF['SamplingFeatureName'] = '{0} ({1}) {2} Soil Sample, LabID {3}'.format(
            row['name'], row['code'], depth_str, row['LabID'])
        SF['SamplingFeatureDescription'] = '{0} (Site {1}), {2} Soil Depth Interval (core section), LabID {3}, at {4} CZO'.format(
            row['name'], row['code'], depth_str, row['LabID'], row['czo'])

        # attr for specimens
        SF['SpecimenTypeCV'] = 'Core section'
        SF['SpecimenMediumCV'] = 'Soil'
        SF['IsFieldSpecimen'] = True
        sf_object = odm2mod.Specimens(**SF)

    return sf_object


def create_action(row, SF_set):
    """
    Function to create Action
    :row:    Row of dataframe
    :SF_set: Type of Sampling Features
    """

    ACT = dict()

    datetime_assign = datetime.datetime.strptime('{} 12:00'.format(row['collectiondate']),
                                                 '%Y-%m-%d %H:%M')
    ACT['BeginDateTime'] = datetime_assign
    ACT['BeginDateTimeUTCOffset'] = -8  # hardwired placeholder
    ACT['EndDateTime'] = datetime_assign
    ACT['EndDateTimeUTCOffset'] = -8  # hardwired placeholder

    # Use of hard-coded MethodID values could be replaced with use of MethodCode string,
    # plus a database query to get the matching MethodID
    if SF_set == 'site':
        ACT['ActionTypeCV'] = 'Generic non-observation'
        ACT['MethodID'] = 29
        ACT['ActionDescription'] = '{}, populate Site Sampling Feature'.format(row['code'])
    elif SF_set == 'profile':
        ACT['ActionTypeCV'] = 'Site visit'
        ACT['MethodID'] = row['coringmethodid']
        ACT['ActionDescription'] = '{}, populate profile (core) Sampling Feature'.format(row['code'])
    elif SF_set == 'coresection':
        ACT['ActionTypeCV'] = 'Specimen collection'
        # HMM, it's clear that 18 (Soil Auger Core) wasn't the appropriate method for soil auger 'profile'
        # But I'll use it for both the profile and the core section here, for now. TO BE FIXED LATER
        MethodID = {15: 17, 18: 18}[row['coringmethodid']]
        ACT['MethodID'] = MethodID
        depth_str = row['Depth'] + 'cm'
        ACT['ActionDescription'] = '{0}, collected soil depth interval (core section) sample at ({1})'.format(
            row['code'], depth_str)

    return odm2mod.Actions(**ACT)


def create_actionby(row, ActionID):
    """
    Function to create ActionBy
    * Requires no changes to handle both sites and cores. *
    :row:    Row of dataframe
    :ActionID: Action ID to assign action by
    """

    ACTBY = dict()

    ACTBY['ActionID'] = ActionID
    ACTBY['AffiliationID'] = row['actionbyaffiliationid']
    ACTBY['IsActionLead'] = True
    # ACTBY['RoleDescription'] = 'xxxx'

    return odm2mod.ActionBy(**ACTBY)


def create_featureaction(row, ActionID, SamplingFeatureID):
    """
    Function to create Feature Action
    * Requires no changes to handle both sites and cores. *
    :row:    Row of dataframe
    :ActionID: Action ID to assign action by
    :SamplingFeatureID: Sampling Feature ID To link action to sampling feature
    """

    FACT = dict()

    FACT['SamplingFeatureID'] = SamplingFeatureID
    FACT['ActionID'] = ActionID

    return odm2mod.FeatureActions(**FACT)


def create_igsn(row, SamplingFeatureID, IGSN_ExternalIdentifierSystemID, SF_set):
    """
    Function to create IGSN's
    :row: Row of dataframe
    :SamplingFeatureID: Sampling Feature ID to connect with IGSN
    :IGSN_ExternalIdentifierSystemID: External Identifier System ID for IGSN
    :SF_set: Type of Sampling Features
    """

    IGSN = dict()

    IGSN['SamplingFeatureID'] = SamplingFeatureID
    IGSN['ExternalIdentifierSystemID'] = IGSN_ExternalIdentifierSystemID

    if SF_set == 'coresection':
        igsn_code = row['IGSN']
    else:
        igsn_code = {'site': row['siteigsn'], 'profile': row['coreigsn']}[SF_set]
    IGSN['SamplingFeatureExternalIdentifier'] = igsn_code
    IGSN['SamplingFeatureExternalIdentifierURI'] = 'https://app.geosamples.org/sample/igsn/{}'.format(igsn_code)

    return odm2mod.SamplingFeatureExternalIdentifiers(**IGSN)


def create_relatedfeatures(row, SamplingFeatureID, SF_set, DBSession):
    """
    Function to create Related Features
    :row: Row of dataframe
    :SamplingFeatureID: Sampling Feature ID to connect with another SF
    """

    RSF = dict()

    RSF['SamplingFeatureID'] = SamplingFeatureID
    RSF['RelationshipTypeCV'] = 'Is child of'  # or 'Was collected at'
    SamplingFeatureCode = {'profile': row['code'], 'coresection': row['code'] + '-profile'}[SF_set]
    ParentSF_ID = DBSession.query(odm2mod.SamplingFeatures).filter(
        odm2mod.SamplingFeatures.SamplingFeatureCode == SamplingFeatureCode
    ).one().SamplingFeatureID
    RSF['RelatedFeatureID'] = ParentSF_ID

    return odm2mod.RelatedFeatures(**RSF)


def create_sfextpropvalues(PropertyID, PropertyValue, SamplingFeatureID):
    """
    Function to create Sampling Feature Extension Property Values
    :PropertyID: Property ID of extension property
    :PropertyValue: Actual value for the extension property
    :SamplingFeatureID: Sampling Feature ID to connect with extension property values
    """

    SFEPV = dict()

    SFEPV['SamplingFeatureID'] = SamplingFeatureID
    SFEPV['PropertyID'] = PropertyID
    SFEPV['PropertyValue'] = str(PropertyValue)

    return odm2mod.SamplingFeatureExtensionPropertyValues(**SFEPV)


def update_featuregeometry(DBSession):
    sql_str = 'UPDATE SamplingFeatures SET FeatureGeometry = ST_PointFromText(FeatureGeometryWKT, 4326)'

    DBSession.execute(sql_str)

    DBSession.commit()


def cleanup(DBSession):
    """
    Function to clean up database during testing, clears out Sampling Features and Actions
    """

    # Delete Sampling Features (with cascade delete)
    _delete_table(odm2mod.SamplingFeatures, DBSession)

    # Delete Actions (with cascade delete)
    _delete_table(odm2mod.Actions, DBSession)


def _delete_table(table, DBSession):
    for r in DBSession.query(table).all():
        DBSession.delete(r)

        DBSession.commit()
