import datajoint as dj

schema = dj.schema(dj.config.get('database.prefix', '') + 'ibl_reference')

@schema
class Lab(dj.Lookup):
    # <class 'misc.models.Lab'>
    definition = """
    lab_name:           varchar(255)  # name of lab
    ---
    lab_uuid:           varchar(64)
    institution:        varchar(255)  
    address:            varchar(255)
    time_zone:          varchar(255)
    """

@schema
class LabMember(dj.Manual):
    # <class 'misc.models.LabMember'>
    # <class 'django.contrib.auth.models.User'>
    definition = """
    user_name:		        varchar(255)	# username
    ---
    user_uuid:              varchar(64)     
    password:		        varchar(255)	# password
    email=null:		        varchar(255)	# email address
    last_login=null:	    datetime	    # last login
    first_name=null:        varchar(255)	# first name
    last_name=null:		    varchar(255)	# last name
    date_joined:	        datetime	    # date joined
    is_active:		        boolean		    # active
    is_staff:		        boolean		    # staff status
    is_superuser:	        boolean		    # superuser status
    is_stock_manager:       boolean         # stock manager status
    groups=null:            blob            # 
    user_permissions=null:   blob            #
    """

@schema
class LabMembership(dj.Manual):
    definition = """
    -> Lab
    -> LabMember
    ---
    lab_membership_uuid:    varchar(64)
    role=null:              varchar(255)
    mem_start_date=null:    date
    mem_end_date=null:      date
    """
@schema
class LabLocation(dj.Manual):
    # <class 'misc.models.LabLocation'>    
    definition = """
    # The physical location at which an session is performed or appliances are located.
    # This could be a room, a bench, a rig, etc.
    -> Lab
    location_name:      varchar(255)    # name of the location
    ---
    location_uuid:      varchar(64)
    """

@schema
class Project(dj.Lookup):
    definition = """
    project_name:               varchar(255)
    ---
    project_uuid:               varchar(64)
    project_description=null:   varchar(1024)
    """

@schema 
class ProjectLabMember(dj.Manual):
    definition = """
    -> Project
    -> LabMember
    """

@schema
class ProjectRepository(dj.Computed):
    definition = """
    -> Project
    -> data.DataRepository
    """

@schema
class Severity(dj.Lookup):
    definition = """
    severity:			tinyint			# severity
    ---
    severity_desc:		varchar(32)		# severity desc
    """
    contents = (
        (0, ''),
        (1, 'Sub-threshold'),
        (2, 'Mild'),
        (3, 'Moderate'),
        (4, 'Severe'),
        (5, 'Non-recovery'),
    )

@schema
class Note(dj.Manual):
    # <class 'misc.models.Note'>
    # TODO: tagging arbitrary objects..
    definition = """
    -> LabMember
    note_uuid:      varchar(64)
    ---
    date_time:		datetime		# date time
    text=null:		varchar(255)	# text
    object_id:		varchar(64)		# object id
    content_type:   varchar(8)
    text=null:      varchar(1024)    
    image=null:     longblob
    """

@schema
class BrainLocationAcronym(dj.Lookup):
    definition = """
    acronym:  varchar(32) # acronym of a brain location
    ---
    full_name = null: varchar(128) # full name of the brain location
    """
    contents = [
        ['ACA', 'Anterior cingulate area'],
        ['ACB', 'Nucleus accumbens'],
        ['IC', 'Inferior colliculus '],
        ['MOs', 'Secondary motor area'],
        ['MRN', 'Midbrain reticular nucleus'],
        ['root', ''],
        ['RSP', 'Retrosplenial area'],
        ['SCsg', 'Superficial gray layer '],
        ['VISp', 'Primary visual area']
    ]
