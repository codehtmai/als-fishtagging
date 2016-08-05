__author__ = 'doc'

from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.sql import sqltypes
from sqlalchemy import distinct

#Create and engine and get the metadata

##### Import Setup
ImportBase = declarative_base()
import_engine = create_engine('postgresql://djangodb:@Django!@192.168.1.160:5432/fishtagging_import')
import_metadata = MetaData(bind=import_engine)

#### Export Setup
Export_Base = declarative_base()
export_engine = create_engine('postgresql://djangodb:@Django!@192.168.1.160:5432/djangomap')
export_metadata = MetaData(bind=export_engine)



# Import Tables
class tblSpecies(ImportBase):
    __table__ = Table('tblSpecies', import_metadata, autoload=True)

class tblDisposition(ImportBase): # pk problems
    __table__ = Table('tblDisposition', import_metadata, autoload=True)

class tblLandLocation(ImportBase): # pk problems
    __table__ = Table('tblIn/Offshore/Inland', import_metadata, autoload=True)

class tblRecapture(ImportBase):
    #__table__ = Table('tblRecapture', import_metadata, autoload=True)
    __tablename__ = 'tblRecapture'
    __table_args__ = {'autoload': True,'autoload_with': import_engine}
    LastName = Column('Last Name', String) # Rename it
    FirstName = Column('First Name', String)
    tagno = Column('Tag#', sqltypes.Integer)
    crossRefTag = Column('Cross Ref Tag #',sqltypes.Integer)
    releaseNo = Column('release #',sqltypes.Integer)
    member = Column('Member Y/N',String)


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
    tagno = Column('Tag #', sqltypes.Integer)
    SpeciesCode = Column('Species Code',sqltypes.Integer)
    place = Column('Place Tagged',String)
    crossRefTag = Column('Cross Ref Tag #',sqltypes.Integer)
    releaseNo = Column('Release #',sqltypes.Integer)


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
    # imports users from the masters taggers table
    list = import_session.query(tblTaggersMaster).all()

    for item in list:
        #print item.TaggersMasterID, item.__dict__.get('First Name'), item.__dict__.get('Last Name')

        add_user(
            taggersMasterID=item.TaggersMasterID,
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
            stateName=item.St) # State Name

    # TODO: Also scan through and add Recapture users that are missing from TaggersMaster; there are only 6.
    # TODO: Make this de-duplicate. There are 7 users in here twice. See: Larry Gonnello

def add_user(first,last,address1,address,muni,zip,email,phone,cell,business,member,duesDueDate,dateJoined,clubName,
             clubMember,starting,updating,total,stateName,taggersMasterID=None,suffix=None,prefix=None,nick=None):
    # Inserts a new user into the fishtagging_taggers table no matter what
    # Taggers Master Id will only come from the exsiting TblTaggers

    if not member:
        # Boolean field, default to False for now
        # TODO: Investigate if this should be null/blank
        member = False
    if not clubMember:
        clubMember = False

    if not taggersMasterID:
        taggersMasterID = -999

    stateId = stateValToPK(stateName)

    newEntry = fishtagging_taggers(
        taggersMasterID=taggersMasterID,
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

def check_and_add_user(first,last,address1,address=None,muni=None,zip=None,email=None,phone=None,cell=None,business=None
            ,member=None,duesDueDate=None,dateJoined=None,clubName=None, clubMember=None,starting=None,updating=None,
            total=None,stateName=None,taggersMasterID=None,suffix=None,prefix=None,nick=None):
    # Will only call add_user if the first, last and suffix don't match anything

    userid = None

    if first == None or first == '' or last == None or last =='':
        return None
    userQuery = export_session.query(fishtagging_taggers).filter(fishtagging_taggers.first == first, fishtagging_taggers.last == last,
                                                            fishtagging_taggers.suffix == check_string(suffix))
    usersCount = userQuery.count()
    if usersCount == 0: # add new user
        userid = add_user(first,last,address1,address,muni,zip,email,phone,cell,business,member,duesDueDate,dateJoined,clubName,
        clubMember,starting,updating,total,stateName,taggersMasterID,suffix,prefix,nick)
        #print "User #{} inserted".format(userid)
    elif usersCount ==1:
        userid = userQuery.first().id
    else:
        print "Strange; userscount:{}, first:{},last:{},suffix:{},taggersMasterID:{},userid:{}".format(usersCount,first,last,suffix,taggersMasterID,userid)


    return userid

def transfer_tags():
    # transfers users and tags from tblTags
    print "Initiating transfer"
    i = 0
    for item in import_session.query(tblTags).yield_per(100).enable_eagerloads(False):
        userid = check_and_add_user(
            first=item.FirstName,
            last=item.LastName,
            suffix=item.Suffix,
            #prefix=check_string(item.Prefix), # Commented items are not in tblTags
            #nick=check_string(item.First),
            #address1=check_string(item.__dict__.get('Address Line 1')),
            address1=item.Address,
            muni=item.Munic,
            zip= item.zip,
            #email= check_string(item.email),
            #phone= check_string(item.Phone),
            #cell= check_string(item.Cell),
            #business= check_string(item.Business),
            #member=item.Member == 1, # Casting from the Access Y/N
            #duesDueDate=item.Dues,
            #dateJoined=item.__dict__.get('Date Joined'),
            clubName=item.ClubName,
            #clubMember=item.__dict__.get('Club Member') == 1,
            #starting=item.Starting,
            #updating=item.Updating,
            #total=item.Total,
            stateName=item.St
        )
        #if isinstance(userid, ( int, long ) ):
        # proceed allowing null users for now ###
        insert_tag(
            item.tagno,
            item.Date,
            item.place,
            item.Length,
            item.oz,
            item.Weight,
            item.WH, # int this is a yes/no (1/0) in access, default no
            item.crossRefTag,
            item.releaseNo,
            item.Daterun,
            item.Latitude,
            item.Longitude,
            item.SpeciesCode,
            userid,
            item.zone, # yes this is right
            item.Comments,
            None, # disposition not in tblTags
            False, # not from the recap table
            item.location, # watch for vals
        ) # location field seems to be the id for the legend field, but has values above 2.
        #else:
        #    print "Something very wrong with userID at {}!".format(i)

        i+=1
        if not i%1000:
            print "Completed {} tag transfers".format(i)
        #print userid

def transfer_recaptures():
    # transfers users and tags from tblTags
    print "Initiating recaptures transfer"
    i = 0
    y=0
    for item in import_session.query(tblRecapture).yield_per(100).enable_eagerloads(False):

        if item.member and item.member.upper() == 'YES':
            item.member = True
        else:
            item.member = False

        userid = check_and_add_user(
            first=item.FirstName,
            last=item.LastName,
            suffix=item.Suffix,
            #prefix=check_string(item.Prefix), # Commented items are not in tblTags
            #nick=check_string(item.First),
            #address1=check_string(item.__dict__.get('Address Line 1')),
            address1=item.Address,
            muni=item.Munic,
            zip= item.Zip,
            email= check_string(item.email),
            phone= check_string(item.Phone),
            #cell= check_string(item.Cell),
            #business= check_string(item.Business),
            member=item.member, # Member is a string in tblRecapture
            #duesDueDate=item.Dues,
            #dateJoined=item.__dict__.get('Date Joined'),
            #clubName=item.ClubName,
            #clubMember=item.__dict__.get('Club Member') == 1,
            #starting=item.Starting,
            #updating=item.Updating,
            #total=item.Total,
            stateName=item.St
        )
        #if isinstance(userid, ( int, long ) ):
        # proceed allowing null users for now ###
        insertedtagid=insert_tag(
            item.tagno,
            item.Date,
            item.Place,
            item.Length,
            item.oz,
            item.Weight,
            item.WH, # int this is a yes/no (1/0) in access, default no
            item.crossRefTag,
            item.releaseNo,
            item.WHdaterun, #is this the same as WHDaterun or undaterun?
            item.Latitude,
            item.Longitude,
            None, # no species here..hm
            userid,
            item.zone, # yes this is right
            item.Comments,
            item.DispositionNumber,
            True, # from the recap table
            item.location, # watch for vals
        ) # location field seems to be the id for the legend field, but has values above 2.
        #else:
        #    print "Something very wrong with userID at {}!".format(i)

        i+=1
        if not i%1000:
            print "Completed {} recapture transfers".format(i)

        if insertedtagid:
            y+=1
            print "Completed {} recapture actual inserts".format(y)
        #print userid

def insert_uniquefish():
    newEntry = fishtagging_uniquefish()
    export_session.add(newEntry)
    export_session.flush()
    return newEntry.id

def insert_tag(tagno,date,place,length,oz,weight,wh,crossRefTag,releaseno,daterun,lat,long,species_id,tagger_id,
               whzone_id,comments,disposition_id,isRecapture,location_id):

    #Does tag exist?
    existingTag=export_session.query(fishtagging_tags).filter(fishtagging_tags.tagno == tagno).limit(1).first()

    if existingTag:
        uniqueFishId = existingTag.uniqueFish_id
        if isRecapture: # get the species from a previous tag entry
            species_id = existingTag.species_id

    # Is it mentioned in other tags, even if it hasn't been inserted yet?
    referencedTagRow=export_session.query(fishtagging_tags).filter(fishtagging_tags.crossRefTag == tagno).limit(1).first()

    if referencedTagRow:
        referencedTag = referencedTagRow.tagno
        uniqueFishId = referencedTagRow.uniqueFish_id
        if isRecapture: # get the species from a previous tag entry
            species_id = referencedTagRow.species_id



    # we also need to check the crossref field for previous links so that we can retroactively take the unique id

    if isinstance(crossRefTag,int):
        # alternatively get the unique fish id from a crosstag
        crossRefTagRow=export_session.query(fishtagging_tags).filter(fishtagging_tags.tagno == crossRefTag).limit(1).first()
        if crossRefTagRow: # it might not have been inserted yet.. #TODO: add a method at the end of ETL to rescan for crossrefs. maybe we skip this altogether until then
            uniqueFishId2 = crossRefTagRow.uniqueFish_id
            # sanity check..they should both match if both exist
            #if existingTag:
            #    assert (uniqueFishId == uniqueFishId2) # THis is failing because two tags are separately inserted uniquely. then later the cross rel becomes known
            # to fix it we should write a function HERE TODO search for all tags matching the cross id and reset the unique id to the first one
            uniqueFishId = uniqueFishId2
            if isRecapture:
                species_id = crossRefTagRow.species_id

    if not existingTag:
        if isRecapture:
            #print "WARNING: tagno {} from recapture SKIPPED".format(tagno)
            return None
        uniqueFishId = insert_uniquefish()

    assert(isinstance(uniqueFishId, ( int, long )) ) # make sure we got a unique fish one way or another



    if location_id > 2:
        location_id = None

    #todo: temporary hack. these are missing for some reason
    if species_id in [6, 14, 39, 78, 80, 110, 114, 117, 129, 130, 138, 144, 151, 170, 189, 280, 363, 390, 532, 546, 599, 641, 726, 951]:
        species_id = None

    #Insert new tag
    newEntry = fishtagging_tags(
        tagno  = tagno,
        date = date,
        species_id = species_id,
        place = place,
        location_id = location_id,
        whzone_id = whzone_id,
        disposition_id = disposition_id,
        tagger_id = tagger_id,
        length = length,
        oz = oz,
        weight = weight,
        wh = wh,
        crossRefTag = crossRefTag,
        releaseno  = releaseno,
        daterun = daterun,
        lat  = check_string(lat),
        long  = check_string(long),
        comments = check_string(comments),
        isRecapture = isRecapture,
        uniqueFish_id = uniqueFishId
    )

    export_session.add(newEntry)
    export_session.flush()
    return newEntry.id



def transfer_tags_users():
    print "starting"
    # Get unique first and last names
    #taglist = import_session.query(tblTags.LastName, tblTags.FirstName).group_by(tblTags.LastName, tblTags.FirstName)


    #taglist = import_session.execute('SELECT "tblTags"."First Name", "tblTags"."Tagger Last Name",count(*) as count FROM "tblTags" left join "tblTaggersMaster" on ("tblTaggersMaster"."First Name" = "tblTags"."First Name" AND "tblTaggersMaster"."Last Name" = "tblTags"."Tagger Last Name") where "tblTaggersMaster"."First Name" is null and "tblTaggersMaster"."Last Name" is null group by "tblTags"."First Name", "tblTags"."Tagger Last Name"')
    # lets make them all unique with addresses and take them all

    #taglist = import_session.query(tblTags.LastName, tblTags.FirstName)\
    #.outerjoin(tblTaggersMaster,  tblTaggersMaster.__dict__.get('First Name') == tblTags.FirstName,tblTaggersMaster.__dict__.get('Last Name') == tblTags.LastName)\
    #.filter(tblTaggersMaster.__dict__.get('First Name') == None, tblTaggersMaster.__dict__.get('Last Name') == None)\
    #.group_by(tblTags.LastName, tblTags.FirstName)

    #taglist = import_session.query(tblTags).all()

    taglist = import_session.execute("""
SELECT
  "tblTags"."First Name" AS "firstName",
  "tblTags"."Tagger Last Name" AS "lastName",
  "tblTags"."Suffix",
  "tblTags"."Address",
  "tblTags"."Munic",
  "tblTags"."St",
  "tblTags".zip,
  "tblTags"."Club Name" AS "clubName",
count(*) as count
FROM "tblTags"
--  public."tblTaggersMaster";
left join "tblTaggersMaster" on ("tblTaggersMaster"."First Name" = "tblTags"."First Name" AND
"tblTaggersMaster"."Last Name" = "tblTags"."Tagger Last Name"  )
where "tblTaggersMaster"."First Name" is null and
	"tblTaggersMaster"."Last Name" is null
group by
  "firstName",
  "lastName",
  "tblTags"."Suffix",
  "tblTags"."Address",
  "tblTags"."Munic",
  "tblTags"."St",
  "tblTags".zip,
  "clubName"
  order by "lastName" desc
    """)

    for tag in taglist:
        print "tag"
        stateId = None # Reset
        if tag.firstName is not '' and tag.lastName is not '':
            stateId = stateValToPK(tag.St)
            userId = add_user(tag.firstName,tag.lastName,tag.Address,'',tag.Munic,tag.zip,'','','','',None,None,None,
                tag.ClubName,None,None,None,None,stateId,None,tag.Suffix,None,None)
            print userId

def stateValToPK(stateName):
    # Transforms a state name to the state table's PKID, or returns None

    if stateName is not '':
        stateId = export_session.query(fishtagging_states).filter(fishtagging_states.st == stateName).first() # Turn the State val into the reference PK
        if stateId is not None:
            return stateId.id
        else:
            #print "STATE {} WAS NOT FOUND".format(stateName)
            return None

# lookup stuff for later
# Just going to take the first here..
            #userList = export_session.query(fishtagging_taggers).filter(fishtagging_taggers.first == firstName, fishtagging_taggers.last == lastName)
            #user = userList.first()
            #if user is not None:
                # Get existing user ID
                #userId = user.id
                #print userId


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


def run_transfers():
    transfer_tagtypes()
    transfer_states()
    transfer_landlocation()
    transfer_disposition()
    transfer_species()
    transfer_zonecodes()
    transfer_taggers()
    #transfer_captures()
    transfer_recaptures()


#transfer_taggers()
#transfer_tags()
transfer_recaptures()
#run_transfers()