import time
import datetime




def room():
   
    #from datetime import datetime , date
    return locals()

@auth.requires_login()
def Book():
    date = request.args[0]
    bookId = request.args[1]
    if len(db(db.dict.dictKey==date).select())>0:
        ls = (db(db.dict.dictKey==date).select(db.dict.dictValue))
        l = ls.as_list()[0]['dictValue']
        l.append(bookId)
        #print ls['dictValue']
        db(db.dict.dictKey==date).update(dictValue=l)
    else :
        db(db.dict.update_or_insert(dictKey = date,dictValue = [bookId]))
        #print len(db(db.dict.dictKey==date).select())
    #db(db.dict.update_or_insert(dictKey = date,dictValue = [1,2]))
    return locals()
def date():
    print request.args[0]
    date = request.args[0]
    lis = []
    if len(db(db.dict.dictKey==date).select())>0:
        lis = db(db.dict.dictKey==date).select().as_list()[0]['dictValue']
        print lis
    return locals()


def edit_room():
    grid = SQLFORM.grid(db.room_data)
    return locals()

def edit_events():
    #import time
    #import datetime
    #from datetime import datetime,date
    grid = SQLFORM.grid(db.events1)
    return locals()
def confirm():
    a=request.args(0)
    b=request.args(1)
    c=request.args(2)
    d=request.args(3)
    e=request.args(4)
    f=request.args(5)
    g=request.args(6)
    h=request.args(7)
    i=request.args(8)
    j=request.args(9)
    
    return dict(room=a,start=b,end=c,subject=d,e=e,f=f,g=g,h=h,i=i,j=j  );

def roomprefer():
    form=SQLFORM.factory(Field('start','datetime',requires=IS_NOT_EMPTY()),
                    Field('end','datetime',requires = IS_NOT_EMPTY()),
                    Field('subject','string',requires = IS_NOT_EMPTY()),)
    return locals()



def index():
    rows = db(db.room_data).select()

    return locals();


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission|('read','table name',record_id)
    to decorate functions that need access control
    """

    auth.settings.login_onvalidation = []
    return dict(form=auth())

@auth.requires_login()
def userpreference():
    rows2=[];
    import time;
    import datetime;
    m=datetime.datetime.today()
    form=SQLFORM.factory(Field('Room_number','string',requires = IS_IN_DB( db, 'room_data.room_no' )),
                    Field('From','datetime',requires = IS_DATETIME_IN_RANGE(m)),
                    Field('to','datetime',requires = IS_DATETIME_IN_RANGE(m)),
                    Field('subject','string',requires = IS_NOT_EMPTY()),
                    Field('seats_required','integer',requires = IS_NOT_EMPTY()))
    if(request.args(0)=='0'):
        
        form.vars.Room_number = 'room_1'
    else:
        a=request.args(1)
        args=request.args(0)
        form.vars.seats_required=a
        form.vars.Room_number = args
    if form.process().accepted:
        if form.vars.to < form.vars.From :
            #raise error_message
            #form.vars.to.error_message="errors"
            response.flash='Oops! You have entered an invalid date'
        else:
            rows = db(db.events1.room_no==form.vars.Room_number).select()

            flag=True;
            for row in rows:
                #print row.starts1;
                #print form.vars.from1;
                #print type(row.starts1);
                x= datetime.datetime.strptime(str(form.vars.From),"%Y-%m-%d %H:%M:%S");
                #print x;
                y= datetime.datetime.strptime(str(form.vars.to),"%Y-%m-%d %H:%M:%S");
                print type(x);
           
                if  (  (  (x >row.starts1 and x< row.stops1)or(y>row.starts1 and y < row.stops1)) or ( (x <row.starts1 and x< row.stops1)and (y>row.starts1 and y > row.stops1))  ):
                    flag=False
        
            redirect(URL('best_results', vars=dict( a=form.vars.Room_number, b = form.vars.From , c= form.vars.to, d = form.vars.seats_required ,flag1=flag,subject=form.vars.subject  )  ))
        
    return locals();



def best_results():
    rows2=[];
    xx=[];
    vars = request.get_vars
    import time;
    import datetime;
    print vars.flag1,"000000"
    x= datetime.datetime.strptime(vars.b,"%Y-%m-%d %H:%M:%S");
            #print x;
    y= datetime.datetime.strptime(vars.c,"%Y-%m-%d %H:%M:%S");
    
    rows1= db(vars.d <= db.room_data.seats and db.room_data.room_no!=vars.a ).select()
    rows3= db(db.events1.id>0 and db.events1.room_no!=vars.a).select()
    i=0;
    xx = db(db.room_data.room_no==vars.a).select()
    if(vars.flag1=="True"):
        rows2.append(xx[0])
      
    
    
    for k in rows1:
        print k.room_no
        flag1=True
        for row in rows3:
            
            if  ( (row.room_no == k.room_no) and  ((  (x >row.starts1 and x< row.stops1)or(y>row.starts1 and y < row.stops1)) or ( (x                                 <row.starts1 and x< row.stops1)and (y>row.starts1 and y > row.stops1)))):
                flag1=False;
                break
                    #rows2.append( db(db.events1.id == row.id).select())
        if flag1==True:
            rows2.append(k);
    print rows2;
    return dict(result=rows2,start_time = vars.b,stop_time= vars.c,subject=vars.subject,a=vars.a,b=vars.b,c=vars.c,d=vars.d,flag1=vars.flag1,sub=vars.subject);

def room_results():
    rows2=[];
    xx=[];
#   vars = request.get_vars
    import time;
    import datetime;
    e=request.args(0)
    f=request.args(1)
    g=request.args(2)
    h=request.args(3)
    i=request.args(4)
    j=request.args(5)
    
    f=f.replace("_"," ",1)
    f=f.replace("_",":")
    g=g.replace("_"," ",1)
    g=g.replace("_",":")
    
#   print vars.flag1,"000000"
    x= datetime.datetime.strptime(f,"%Y-%m-%d %H:%M:%S");
            #print x;
    y= datetime.datetime.strptime(g,"%Y-%m-%d %H:%M:%S");
    
    rows1= db(h <= db.room_data.seats and db.room_data.room_no!=e ).select()
    rows3= db(db.events1.id>0 and db.events1.room_no!=e).select()
    
    xx = db(db.room_data.room_no==e).select()
    if(i=="True"):
        rows2.append(xx[0])
      
    
    
    for k in rows1:
        print k.room_no
        flag1=True
        for row in rows3:
            
            if  ( (row.room_no == k.room_no) and  ((  (x >row.starts1 and x< row.stops1)or(y>row.starts1 and y < row.stops1)) or ( (x<row.starts1 and x< row.stops1)and (y>row.starts1 and y > row.stops1)))):
                flag1=False;
                break
                    #rows2.append( db(db.events1.id == row.id).select())
        if flag1==True:
            rows2.append(k);
    print rows2;
    return dict(result=rows2,start_time =f,stop_time= g,subject=j,a=e,b=f,c=g,d=h,flag1=i,sub=j);


def show():
    
    a =request.args(0, cast=int )
    b = request.args(1)
    c = request.args(2)
    import time;
    import datetime;
    
    x= datetime.datetime.strptime(b,"%Y-%m-%d_%H_%M_%S");
            #print x;
    y= datetime.datetime.strptime(c,"%Y-%m-%d_%H_%M_%S");
    db.events1.insert(room_no= a, starts1=x , stops1=y,faculty= auth.user.first_name)
    return str(" you have successfully booked" )

def history():
    
    form=SQLFORM.factory(Field('room_number',requires = IS_IN_DB( db, 'room_data.room_no' )))
    if form.process().accepted:
        rows3= db(db.events1.faculty == auth.user.first_name  ).select()
        r1=[]
        for row in rows3:
            print row.starts1.date() , request.now.date()
            if(row.room_no==form.vars.room_number):
                
                if(row.starts1.date() < request.now.date()):
                    r1.append(row)
        
        
        
        
        
        
    else:
        
        rows3= db(db.events1.faculty == auth.user.first_name ).select()
        r1=[]
        for row in rows3:
            print row.starts1.date() , request.now.date()
            if(row.starts1.date() < request.now.date()):
                r1.append(row)
    
    
    
    return dict(history=r1,form=form)

def upcomingevents():
    rows3= db(db.events1.faculty == auth.user.first_name ).select()
    r1=[]
    for row in rows3:
        print row.starts1.date() , request.now.date()
        if(row.starts1.date() >= request.now.date()):
            r1.append(row)
    
    
    
    return dict(history=r1)

@auth.requires_login()
def loggedin():
    return locals();





def book():
    name= request.args(0)
    start=request.args(1)
    stop=request.args(2)
    subject= request.args(3)
    
    start=start.replace("_"," ",1)
    start=start.replace("_",":")
    stop=stop.replace("_"," ",1)
    stop=stop.replace("_",":")
    
    db.events1.insert(room_no=name,starts1=start,stops1=stop,faculty= auth.user.first_name,course=subject)
    print start,stop,subject
    return dict(a=name,b=start,c=stop,d= auth.user.first_name,e=subject);
def cancel():
    arg=request.args[0]
    del db.events1[arg]
    redirect(URL('upcomingevents'  ))
    return


@auth.requires_membership('admin')
def admin():
       return locals()
