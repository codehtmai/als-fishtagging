from django.db import models

class Species(models.Model):
    code = models.IntegerField(unique=True)  # may just need to import as the PK?
    species = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.species

class Disposition(models.Model):
    disposition = models.CharField(max_length=25)

    def __str__(self):              # __unicode__ on Python 2
        return self.disposition

class LandLocation(models.Model):
    legend = models.CharField(max_length=8)

    def __str__(self):              # __unicode__ on Python 2
        return self.legend

class States(models.Model):
    st = models.CharField(max_length=2)

    def __str__(self):              # __unicode__ on Python 2
        return self.st

class WHZoneCodes(models.Model):
    zoneno = models.CharField(max_length=5) # This might need to be an Int PK that gets loaded in
    masterzone = models.CharField(max_length=2, blank=True)
    description = models.CharField(max_length=80, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.zoneno

class TagTypes(models.Model):
    typenum = models.IntegerField() # Again..this might just be the imported PKs
    tagtype = models.CharField(max_length=12)
    lotsize = models.IntegerField(blank=True, null=True)
    lotprice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    needleprice = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.tagtype

class TagPurchases(models.Model):
    tagpurchaseid = models.IntegerField()
    purchasedate = models.DateTimeField()
    tagstart = models.IntegerField()
    tagend = models.IntegerField()
    #tagtype = models.IntegerField() # type and tagType are in the original schema but don't seem to need both.
    type = models.ForeignKey(TagTypes)
    numberOfKits = models.IntegerField(blank=True, null=True)
    numberOfNeedles = models.IntegerField(blank=True, null=True)
    purchaseAmount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    postageHandling = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    newMember = models.BooleanField(default=True, blank=True)
    comment = models.CharField(max_length=200, blank=True)
    memberName = models.IntegerField() # TODO: Update with the users table!

class Taggers(models.Model):
    taggersMasterID = models.IntegerField(blank=True) # Refers back to the original TaggersMaster PK from import.
    first = models.CharField(max_length=30, blank=True)
    last = models.CharField(max_length=30)
    suffix = models.CharField(max_length=10, blank=True)
    prefix = models.CharField(max_length=10, blank=True)
    nick = models.CharField(max_length=30, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    muni  = models.CharField(max_length=30, blank=True)
    st = models.ForeignKey(States,blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=14, blank=True)
    cell = models.CharField(max_length=14, blank=True)
    business = models.CharField(max_length=14, blank=True)
    member = models.BooleanField(default=False) # TODO:Calculation - If (dues blank, no, yes)
    duesDueDate = models.DateTimeField(blank=True, null=True)
    dateJoined = models.DateTimeField(blank=True, null=True)
    clubName = models.CharField(max_length=50, blank=True)
    clubMember = models.BooleanField(blank=True)
    starting = models.IntegerField(blank=True, null=True)
    updating = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return "{}, {}".format(self.last, self.first)


class Recapture(models.Model): # Do not use this table
    tagno = models.IntegerField(blank=True, null=True)
    releaseno = models.IntegerField(blank=True, null=True) # How many times it's been released
    date = models.DateTimeField(blank=True, null=True)
    place= models.CharField(max_length=255, blank=True) # Text description of place
    location = models.IntegerField(blank=True, null=True) # TblLocation duplicate of Legend field
    whzone = models.ForeignKey(WHZoneCodes)
    legend = models.ForeignKey(LandLocation)
    disposition = models.ForeignKey(Disposition)
    tagger = models.ForeignKey(Taggers)
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    oz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True)
    tagged = models.CharField(max_length=255, blank=True) # ?
    un = models.CharField(max_length=255, blank=True) #?
    undaterun = models.DateTimeField(blank=True, null=True) #?
    wh = models.CharField(max_length=255, blank=True) #?
    crossRefTag = models.IntegerField(blank=True, null=True) # Get better desc
    whdaterun = models.DateTimeField(blank=True, null=True) # ?
    lat  = models.CharField(max_length=255, blank=True) # todo: update with appropriate field type
    long  = models.CharField(max_length=255, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return "{}, {}".format(self.date, self.place)

class UniqueFish(models.Model):
    #species = models.ForeignKey(Species) # Probably shouldn't use this
    def __str__(self):              # __unicode__ on Python 2
        return "Unique #{}".format(self.pk)

class Tags(models.Model): # Table to contain all captures/releases/recaptures
    tagno  = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    species = models.ForeignKey(Species,to_field="code",blank=True,null=True)
    place = models.CharField(max_length=255, blank=True)
    location = models.ForeignKey(LandLocation,null=True,blank=True)
    whzone = models.ForeignKey(WHZoneCodes,null=True,blank=True)
    disposition = models.ForeignKey(Disposition,null=True,blank=True)
    tagger = models.ForeignKey(Taggers,null=True,blank=True) # for now
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    oz = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    wh = models.CharField(max_length=255, blank=True) #? this is a yes/no 1/1 about sending data to Woods Hall
    crossRefTag = models.IntegerField(blank=True, null=True) # Get better desc
    releaseno  = models.IntegerField(blank=True, null=True)
    daterun = models.DateTimeField(blank=True, null=True)
    lat  = models.CharField(max_length=255, blank=True) # todo: update with appropriate field type
    long  = models.CharField(max_length=255, blank=True)
    comments = models.CharField(max_length=255, blank=True)
    isRecapture = models.BooleanField(default=False)
    uniqueFish = models.ForeignKey(UniqueFish)

    def __str__(self):              # __unicode__ on Python 2
        return "{}, {}".format(self.date, self.place)

    class Meta:
        ordering = ('tagno',)



