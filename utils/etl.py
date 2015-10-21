__author__ = 'doc'

from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy import distinct

#Create and engine and get the metadata

##### Import Setup
ImportBase = declarative_base()
import_engine = create_engine('postgresql://djangodb:@Django!@192.168.1.25:5432/fishtagging_import')
import_metadata = MetaData(bind=import_engine)

#### Export Setup
Export_Base = declarative_base()
export_engine = create_engine('postgresql://djangodb:@Django!@192.168.1.25:5432/djangomap')
export_metadata = MetaData(bind=export_engine)



# Import Tables
class tblSpecies(ImportBase):
    __table__ = Table('tblSpecies', import_metadata, autoload=True)

class tblDisposition(ImportBase): # pk problems
    __table__ = Table('tblDisposition', import_metadata, autoload=True)

class tblLandLocation(ImportBase): # pk problems
    __table__ = Table('tblIn/Offshore/Inland', import_metadata, autoload=True)

class tblRecapture(ImportBase):
    __table__ = Table('tblRecapture', import_metadata, autoload=True)

class tblStates(ImportBase):
    __table__ = Table('tblStates', import_metadata, autoload=True)

class tblTagPurchases(ImportBase):
    __table__ = Table('tblTagPurchases', import_metadata, autoload=True)

class tblTagTypes(ImportBase):
    __table__ = Table('tblTagTypes', import_metadata, autoload=True)

class tblTaggersMaster(ImportBase):
    __table__ = Table('tblTaggersMaster', import_metadata,Column('Last Name', ), autoload=True)

class tblTags(ImportBase):
#    __table__ = Table('tblTags', import_metadata, autoload=True)
    __tablename__ = 'tblTags'
    __table_args__ = {'autoload': True,'autoload_with': import_engine}
    LastName = Column('Tagger Last Name', String) # Rename it
    FirstName = Column('First Name', String)
    ClubName = Column('Club Name', String)


class tblWH_ZoneCodes(ImportBase):
    __table__ = Table('tblWH_ZoneCodes', import_metadata, autoload=True)


# Export Tables
class fishtagging_species(Export_Base):
    __table__ = Table('fishtagging_species', export_metadata, autoload=True)

class fishtagging_disposition(Export_Base):
    __table__ = Table('fishtagging_disposition', export_metadata, autoload=True)

class fishtagging_landlocation(Export_Base):
    __table__ = Table('fishtagging_landlocation', export_metadata, autoload=True)

class fishtagging_states(Export_Base):
    __table__ = Table('fishtagging_states', export_metadata, autoload=True)

class fishtagging_tagtypes(Export_Base):
    __table__ = Table('fishtagging_tagtypes', export_metadata, autoload=True)

class fishtagging_whzonecodes(Export_Base):
    __table__ = Table('fishtagging_whzonecodes', export_metadata, autoload=True)

class fishtagging_taggers(Export_Base):
    __table__ = Table('fishtagging_taggers', export_metadata, autoload=True)

class fishtagging_tags(Export_Base):
    __table__ = Table('fishtagging_tags', export_metadata, autoload=True)

class fishtagging_uniquefish(Export_Base):
    __table__ = Table('fishtagging_uniquefish', export_metadata, autoload=True)

#Create a session to use the tables
import_session = create_session(bind=import_engine)
export_session = create_session(bind=export_engine)

#Here I will just query some data using my foreign key relation,  as you would
#normally do if you had created a declarative data mode.
#Note that not all test records have an author so I need to accomodate for Null records


#o.__dict__.get('Species Code')

def transfer_species():
    specieslist = import_session.query(tblSpecies).all()
    for species in specieslist:
        print species.__dict__.get('Species Code'), species.Species
        #stmt = simple_table.insert()

        newSpecies = fishtagging_species(code = species.__dict__.get('Species Code'),
                        species = species.Species)

        export_session.add(newSpecies)
        export_session.flush()

def transfer_disposition():
    list = import_session.query(tblDisposition).all()

    for item in list:
        print item.ID, item.Disposition

        newEntry = fishtagging_disposition(id=item.ID, disposition=item.Disposition)

        export_session.add(newEntry)
        export_session.flush()

def transfer_landlocation():
    list = import_session.query(tblLandLocation).all()

    for item in list:
        print item.Code, item.Legend

        newEntry = fishtagging_landlocation(id = item.Code, legend = item.Legend)

        export_session.add(newEntry)
        export_session.flush()

def transfer_states():
    list = import_session.query(tblStates).all()

    for item in list:
        print item.St

        newEntry = fishtagging_states(st=item.St)

        export_session.add(newEntry)
        export_session.flush()

def transfer_tagtypes():
    list = import_session.query(tblTagTypes).all()

    for item in list:
        print item.TypeNum, item.TagType

        newEntry = fishtagging_tagtypes(typenum = item.TypeNum,
                                        tagtype = item.TagType,
                                        lotsize = item.LotSize,
                                        lotprice = item.LotPrice,
                                        needleprice = item.NeedlePrice,
                                        start = item.Start,
                                        end = item.End)

        export_session.add(newEntry)
        export_session.flush()

def transfer_zonecodes():
    list = import_session.query(tblWH_ZoneCodes).all()

    for item in list:
        print item.__dict__.get('WH Zone No'),  item.MasterZone, item.__dict__.get('Zone Description')
        mz = item.MasterZone
        if mz == None:
            mz = ''
        newEntry = fishtagging_whzonecodes(zoneno = item.__dict__.get('WH Zone No'),
                                           masterzone = mz,
                                           description = item.__dict__.get('Zone Description'))
        export_session.add(newEntry)
        export_session.flush()

def check_string(str):
    '''Preprocessing to ensure null/blanks don't mess up String fields'''
    if str == None:
        return ''
    else:
        return str

def transfer_taggers():
    list = import_session.query(tblTaggersMaster).all()

    for item in list:
        print item.TaggersMasterID, item.__dict__.get('First Name'), item.__dict__.get('Last Name')

        stateId = export_session.query(fishtagging_states).filter(fishtagging_states.st == item.St).first() # Turn the State val into the reference PK
        if stateId is not None:
            stateId = stateId.id
        print str(stateId)

        newEntry = fishtagging_taggers(taggersMasterID=item.TaggersMasterID,
                                       first=check_string(item.__dict__.get('First Name')),
                                       last=item.__dict__.get('Last Name'),
                                       suffix=check_string(item.Suffix),
                                       prefix=check_string(item.Prefix),
                                       nick=check_string(item.First),
                                       address1=check_string(item.__dict__.get('Address Line 1')),
                                       address=check_string(item.Address),
                                       muni=check_string(item.Munic),
                                       zip= check_string(item.Zip),
                                       email= check_string(item.email),
                                       phone= check_string(item.Phone),
                                       cell= check_string(item.Cell),
                                       business= check_string(item.Business),
                                       member=item.Member == 1, # Casting from the Access Y/N
                                       duesDueDate=item.Dues,
                                       dateJoined=item.__dict__.get('Date Joined'),
                                       clubName=check_string(item.ClubName),
                                       clubMember=item.__dict__.get('Club Member') == 1,
                                       starting=item.Starting,
                                       updating=item.Updating,
                                       total=item.Total,
                                       st_id=stateId)
        export_session.add(newEntry)
        export_session.flush()
    # TODO: Also scan through and add Recapture users that are missing from TaggersMaster; there are only 6.
    # TODO: Make this de-duplicate. There are 7 users in here twice. See: Larry Gonnello

def add_user(first,last,address1,address,muni,zip,email,phone,cell,business,member,duesDueDate,dateJoined,clubName,clubMember,starting,updating,total,stateId,taggersMasterId=None,suffix=None,prefix=None,nick=None):
    newEntry = fishtagging_taggers(taggersMasterID=taggersMasterId,
                               first=check_string(first),
                               last=check_string(last),
                               suffix=check_string(suffix),
                               prefix=check_string(prefix),
                               nick=check_string(nick),
                               address1=check_string(address1),
                               address=check_string(address),
                               muni=check_string(muni),
                               zip= check_string(zip),
                               email= check_string(email),
                               phone= check_string(phone),
                               cell= check_string(cell),
                               business= check_string(business),
                               member=member, # Casting from the Access Y/N
                               duesDueDate=duesDueDate,
                               dateJoined=dateJoined,
                               clubName=check_string(clubName),
                               clubMember=clubMember,
                               starting=starting,
                               updating=updating,
                               total=total,
                                st_id=stateId)
    export_session.add(newEntry)
    export_session.flush()
    return newEntry.id

def transfer_tags_users():
    print "starting"
    # Get unique first and last names
    #list = import_session.query(tblTags.LastName, tblTags.FirstName).group_by(tblTags.LastName, tblTags.FirstName)

    taglist = import_session.query(tblTags).all()

    zeroes = 0
    ones = 0
    higher = 0
    for tag in taglist:
        print "tag"
        print tag.LastName
        if tag.FirstName is not '' and tag.LastName is not '':
            # Just going to take the first here..
            userList = export_session.query(fishtagging_taggers).filter(fishtagging_taggers.first == tag.FirstName, fishtagging_taggers.last == tag.LastName)
            user = userList.first()
            if user is not None:
                # Get existing user ID
                userId = user.id
                #print userId
            else:
                stateId = export_session.query(fishtagging_states).filter(fishtagging_states.st == tag.St).first() # Turn the State val into the reference PK
                if stateId is not None:
                    stateId = stateId.id
                else:
                    print "STATE WAS NOT FOUND"

                userId = add_user(tag.FirstName,tag.LastName,tag.Address,'',tag.Munic,tag.zip,'','','','',None,None,None,
                         tag.ClubName,None,None,None,None,stateId,None,tag.Suffix,None,None)
            print userId







    #     num = len([a for a in userId])
    #     if num == 0:
    #         zeroes +=1
    #     elif num == 1:
    #         ones +=1
    #     else:
    #         higher +=1
    #         for g in userId:
    #             print g.id, g.first, g.last
    # print zeroes, ones, higher

def transfer_captures():

    # Get unique first and last name
    list = import_session.query(tblTags.LastName, tblTags.FirstName).group_by(tblTags.LastName, tblTags.FirstName)

    for item in list:
        print item.TaggersMasterID, item.__dict__.get('First Name'), item.__dict__.get('Last Name')

        # Look up tagger #
        taggerId = export_session.query(fishtagging_taggers).filter(fishtagging_taggers.last == item.__dict__.get('Last Name'))
        #print taggerId.id


def transfer_recaptures():
    pass

def run_transfers():
    transfer_tagtypes()
    transfer_states()
    transfer_landlocation()
    transfer_disposition()
    transfer_species()
    transfer_zonecodes()
    transfer_taggers()
    transfer_captures()
    transfer_recaptures()

transfer_tags_users()