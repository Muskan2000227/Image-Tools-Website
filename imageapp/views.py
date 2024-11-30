from django.shortcuts import render,redirect
from imageapp.models import FAQ,myreview,Help,contactme
from imageapp.models import register,article,editor
from django.conf import settings
from django.core.mail import send_mail
from PIL import Image ,ImageFont,ImageDraw,ImageFilter,ImageEnhance,ImageOps
import ntpath
import cv2
#from rembg import remove
 

# Create your views here.
def log(request):
    if request.method=='POST':
        em = request.POST.get('mail')
        passw=request.POST.get('passw')          
        expert=register.objects.filter(email=em,password=passw)
        k=len(expert)
        if k>0:
            request.session['email']=em
            #return render(request,'index.html')
            return redirect('/main')
        else:
            return render(request,'login.html',{'ms':1})
    else:
            return render(request,'login.html')

def logout(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     del request.session['email']
     return redirect('/Login')
          
     
     


def reg(request):
    if request.method=="POST":
        name=request.POST.get('user')
        em=request.POST.get('mail')
        password=request.POST.get('passw')
        cpass=request.POST.get('cpassw')
        value={'name':name,'em':em,'password':password,'cpass':cpass}
        val={'name':name,'password':password,'cpass':cpass}
        
        if register.objects.filter(email=em).exists():
            
            return render(request,'signup.html',{'ms':1,'values':val})
        else:
          if password == cpass:
            try:
              validate_password(password)
            except ValidationError as e:
              error_message = e.messages[0]
              return render(request, 'signup.html', {'ms': 4, 'error_message': error_message,'values':value})
        
            x = register()
            x.name = name
            x.email = em
            x.password = password
            x.save()
            
        
            return render(request, 'signup.html', {'ms': 2})
          else:
             return render(request, 'signup.html', {'ms': 3})
    else:
         return render(request,'signup.html')

def forgot(request):
     if (request.method=="POST"):
          em=request.POST.get('mail')
          user=register.objects.filter(email=em)
          if (len(user)>0):
               pw=user[0].password
               subject="NEW PASSWORD"
               message="Welcome! Your Password is "+pw
               email_from=settings.EMAIL_HOST_USER
               recipient_list=[em]
               send_mail(subject,message,email_from,recipient_list)
               
               return render(request,'forpass.html',{'rest':1})
          else:
               
               return render(request,"forpass.html",{"rest":2})
     else:
          return render(request,"forpass.html")
     
    
def indexes(request):
     data=FAQ.objects.all()
     datas=article.objects.all()
     return render(request,'index.html',{'data':data,'datas':datas})

def foot(request):
    return render(request,'footer.html')

def sidebar(request):
    if not request.session.has_key('email'):
          return redirect('/Login')
    return render(request,'side2.html')

def chngepass(request):
    if not request.session.has_key('email'):
          return redirect('/Login')
    if request.method=='POST':
        re=register.objects.get(email=request.session['email'])
        opassword=request.POST.get('old')
        npassword=request.POST.get('new')
        cpassword=request.POST.get('conf')

        if (npassword==cpassword):
            pa=re.password
            print(pa)
            if opassword==pa:
                re.password=npassword
                re.save()
                
                return render(request,'changepassword.html',{'res':1})
        
            else:
               
                return render(request,'changepassword.html',{'res':2})
        else:
            
            return render(request,'changepassword.html',{'res':3})
    else:
            return render(request,'changepassword.html')

def bas(request):
    return render(request,'base.html')

def faqs(request):
    data=FAQ.objects.all()
    return render(request,'viewfaq.html',{'data':data})

def review(request):
    if not request.session.has_key('email'):
          return redirect('/Login')
    if request.method=="POST":
           x=myreview()
           print("yes")
           x.title=request.POST.get('ti')
           x.message=request.POST.get('msg')
           x.save()
           return render(request,'review.html',{'succ':1})
    else:
           return render(request,'review.html')
    
def Helps(request):
    if not request.session.has_key('email'):
          return redirect('/Login')
    if request.method=="POST":
        x=Help()
        x.title=request.POST.get('ti')
        x.message=request.POST.get('msg')
        x.save()
        return render(request,'HelpSupport.html',{'succ':1})  
    else:
          return render(request,'HelpSupport.html')  

def cont(request):
    if request.method=="POST":
        x=contactme()
        x.name=request.POST.get('user')
        x.email=request.POST.get('mail')
        x.phone=request.POST.get('phone')
        x.message=request.POST.get('msg')
        x.save()
        return render(request,'contact.html',{'succ':1})
    else:
        return render(request,'contact.html')
    

# def cont(request):
#     if request.method=="POST":
#         x=contactme(request.POST)

#         if form.is_valid():
#            print("the form was valid")
#            send_mail('The contact form subj','this is the message','noreply@imagetool27@gmail.com',['imagetool27@gmail.com'])
#            return redirect('contact')
#         else:
#              x=contactme()   
#         return render(request,'contact.html',{'succ':1})
   
    



   
def Editp(request):
    if not request.session.has_key('email'):
          return redirect('/Login')
    user = register.objects.get(email=request.session['email'])
    if request.method == "POST":
        user = register.objects.get(email=request.session['email'])
        user.name = request.POST.get('name')
        user.phoneno=request.POST.get('numb')
        user.Country= request.POST.get('country')
        user.State=request.POST.get('state')
        user.Address=request.POST.get('address')
        user.Pincode=request.POST.get('pin')
        user.detail=request.POST.get('bio')
       
        user.save()
        #data = register.objects.get(email=request.session['email'])
        return redirect('/UserProfile')
       
    else:
     return render(request, 'editprof.html', {'user': user})      

def Userprof(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     user=register.objects.get(email=request.session['email'])
     if request.method == "POST":
          print("yes")
          user.profile=request.FILES['file1']
          user.save()
          """x=request.FILES['file1']
          print("=====================",x)
          import os
          import numpy as np 
          s=os.getcwd(x)
          print(s)"""
          return render(request,'userprofile.html',{'user':user,'msg':'success'})

     else:
          return render(request,'userprofile.html',{'user':user}) 
    
    

def arti(request):
        data=article.objects.all()
        return render(request,'articles.html',{'data':data})

def handle_uploaded_file(f,name):
     destination=open(name,'wb+')
     for chunk in f.chunks():
          destination.write(chunk)
     destination.close()

def img(request):
        return render(request,'mainimg.html')

def res(request):
        return render(request,'result.html')

def txtres(request):
        return render(request,'textresult.html')



def too(request):
        if not request.session.has_key('email'):
          return redirect('/Login')
        return render(request,'tools.html')

def tool(request):
        
        return render(request,'tools2.html')

def editr(request):
     data=editor.objects.all()
     return render(request,'editors.html',{'data':data})

def detblog(request, id):
     data=article.objects.get(id=id)
     return render(request,'detailblog.html',{'data':data})

def imgtxt(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np 
          import pytesseract as tess
          s=os.path.splitext(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1]) 
          #path_to_tesseract="C:\\Users\\MUSKAN SAINI\\AppData\\Local\\Programs\\Tesseract-OCR//tesseract.exe"
          #providing Tesserat execuatble location to pytesserat library
          tess.pytesseract.tesseract_cmd=r'C:\Users\saini\imagetool\Tesseract-OCR\tesseract.exe'
          #Passing img obj to image_To_string
          #This will extract text from image
          img=Image.open('temp'+s[1])
          text=tess.image_to_string(img)
          #Displaying extracted text
          print(text[:-1])
          #open text file
          text_file=open("static/data.txt","w")
          #write string to file
          text_file.write(text)
          #close file
          text_file.close()
          return render(request,'textresult.html',{'txt':text})
     else:
          return render(request,'imgtotxt.html')
     

def cartoon(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          s=os.path.splitext(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          im=Image.open('temp'+s[1])
          import cv2
          import numpy as np
          img=cv2.imread('temp'+s[1])
          def cartoonize(img,k):
               gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
               edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,8)
               data=np.float32(img).reshape((-1,3))
               print("Shape of input data",img.shape)
               print("Shape of resized data",data.shape)
               criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,20,1.0)
               _,label,center=cv2.kmeans(data,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
               center=np.uint8(center)
               result=center[label.flatten()]
               result=result.reshape(img.shape)
               blurred=cv2.medianBlur(result,3)
               cartoon=cv2.bitwise_and(blurred,blurred,mask=edges)
               return cartoon
          cartoonized=cartoonize(img,8)
          cv2.imwrite('static/cartoon'+s[1],cartoonized)
          p='cartoon'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else: 
          return render(request,'catoonify.html')

def facereco(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          import cv2
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          img=np.array(Image.open('temp'+s[1]))
          print('img','temp'+s[1])
          img=cv2.imread('temp'+s[1])
          #Load Haar cascade for face detection
          face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
          gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          #DEtect faces in image
          faces=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
          #Draw rectangles around detected faces
          for(x,y,w,h) in faces:
               cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
               cv2.imwrite('static/facerecog'+s[1],img)
          p='facerecog'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'facerecog.html')
    
  

  
def rem(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          val=float(request.POST.get('bright'))
          img=Image.open('temp'+s[1])
          
          enhancer = ImageEnhance.Brightness(img)
          img1=enhancer.enhance(val)


          img1.save('static/brightness'+s[1])
          p='brightness'+s[1]
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'bright.html')




import PIL
import textwrap
import PIL
from PIL import ImageFont, ImageDraw
import textwrap

def txt(request):
    if not request.session.has_key('email'):
        return redirect('/Login')

    if request.method == "POST":
        font_size = 25
        font = ImageFont.truetype(r"C:\Users\MUSKAN SAINI\image_tool\imageapp/arial.ttf", font_size)
        text = request.POST.get('text')

        # Wrap the text to fit within 50 characters per line
        wrapper = textwrap.TextWrapper(width=50)
        word_list = wrapper.wrap(text=text)

        # Calculate the height of the image based on the number of lines
     #    line_height = font.getsize('hg')[1]  # Height of a line with 'h' and 'g' characters (approximation)
        line_height = font.getbbox('hg')[3]

        image_height = len(word_list) * line_height + 100  # Add some padding

        # Create image and draw object
        image = PIL.Image.new('RGB', (600, image_height))
        draw = PIL.ImageDraw.Draw(image)

        # Draw each line onto the image
        y_offset = 30
        for line in word_list:
            draw.text((20, y_offset), line, font=font, fill='white')
            y_offset += line_height

        image.save("static/output.png")
        p = "output.png"
        print(p)
        return render(request, 'result.html', {'p': p})
    else:
        return render(request, 'txttoimg.html')
 

def bluri(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     return render(request,'blur.html')     

def gblur(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          import cv2
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          if s[1]=="jpg":
               jpg=1
          else:
               jpg=0
          handle_uploaded_file(f,'temp'+s[1])
          img=np.array(Image.open('temp'+s[1]))
          print("img",'temp'+s[1])
          img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
          gausBlur= cv2.GaussianBlur(img,(91,91),0)

          cv2.imwrite('static/gblur'+s[1],gausBlur)
          p='gblur'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'gauss.html')

def mblur(request):
      if not request.session.has_key('email'):
          return redirect('/Login')
      if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          import cv2
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          if s[1]=="jpg":
               jpg=1
          else:
               jpg=0
          handle_uploaded_file(f,'temp'+s[1])
          img=np.array(Image.open('temp'+s[1]))
          print("img",'temp'+s[1])
          img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
          medBlur= cv2.medianBlur(img,51)
          #cv2.imshow('Media blurring',medBlur)
          cv2.imwrite('static/mblur'+s[1],medBlur)
          p='mblur'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
      else:
        return render(request,'median.html')
    

def bblur(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          import cv2
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          if s[1]=="jpg":
               jpg=1
          else:
               jpg=0
          handle_uploaded_file(f,'temp'+s[1])
          img=np.array(Image.open('temp'+s[1]))
          print("img",'temp'+s[1])
          img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
          bilFilter= cv2.bilateralFilter(img,9,75,75)
          #cv2.imshow('Media blurring',medBlur)
          cv2.imwrite('static/later'+s[1],bilFilter)
          p='later'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'bilateral.html')

def greys(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np 
          s=os.path.splitext(f.name)
          print(s[1])
          if s[1]=="jpg":
               jpg=1
          else:
               jpg=0
          handle_uploaded_file(f,'temp'+s[1])   
          img=np.array(Image.open('temp'+s[1]))
          print("img",'temp'+s[1])
          #cvtColor() func to greyscale img
          gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
          cv2.imwrite('static/later'+s[1],gray_img)
          p='later'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,"Greyscale.html")

def resi(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          #n=int(request.POST.get('degree'))
          #print("degree",n)
          import os
          from PIL import Image
          s=os.path.splitext(f.name)
          print(s[1])

          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])
          print("img",'temp'+s[1])
          width=int(request.POST.get('width'))
          height=int(request.POST.get('height'))
          imim=img.resize((width,height))
          imim.save('static/resize'+s[1])
          p='resize'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'resize.html')
      

def rotating(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          n=int(request.POST.get('degree'))
          print("degree",n)
          import os
          from PIL import Image
          s=os.path.splitext(f.name)
          print(s[1])

          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])
          print("img",'temp'+s[1])
          imim=img.rotate(n,expand=True,fillcolor=(0,0,0))
          imim.save('static/rotate'+s[1])
          p='rotate'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'rotate.html')


def enhance(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])

          enhancer = ImageEnhance.Color(img)#vibrance
          img1=enhancer.enhance(2)
          
          #img1=img.filter(ImageFilter.GaussianBlur(radius=20))
          #img1=img.filter(ImageFilter.UnsharpMask(radius=50))


          img1.save('static/edgeenhance'+s[1])
          p='edgeenhance'+s[1]
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'imgenhance.html')  


       

def creategif(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])     
          img=Image.open('temp'+s[1])
          img.save('static/compressed'+s[1], optimize=True, quality=50)
          p='compressed'+s[1]
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
           return render(request,'compress.html') 


    

from PIL import Image

def shift(request):
    if not request.session.has_key('email'):
        return redirect('/Login')

    if request.method == "POST":
        f = request.FILES['file1']
        import os
        s = os.path.splitext(f.name)
        print(s[1])
        handle_uploaded_file(f, 'temp' + s[1])
        img = Image.open('temp' + s[1])
        print("img", 'temp' + s[1])
        shift_x = int(request.POST.get('x'))
        shift_y =int(request.POST.get('y'))
        affine_matrix = (1, 0, shift_x, 0, 1, shift_y)
        # Perform the image shifting
        imim = img.transform(img.size, Image.AFFINE, affine_matrix)

        imim.save('static/rotate' + s[1])
        p = 'rotate' + s[1]
        print("p")
        return render(request, 'result.html', {'p': p})
    else:
        return render(request, 'shifting.html')


def scale(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          border=int(request.POST.get('border'))
          color=str(request.POST.get('color'))
          import os
          from PIL import Image
          s=os.path.splitext(f.name)
          print(s[1])
          
          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])
          print("img",'temp'+s[1])
          imim=ImageOps.expand(image=img,border=border,fill=color)
          imim.save('static/rotate'+s[1])
          p='rotate'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'scaling.html')
     
def edge(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(s[1])
          if s[1]=="jpg":
               jpg=1
          else:
               jpg=0
          handle_uploaded_file(f,'temp'+s[1])
          img=np.array(Image.open('temp'+s[1]))
          print("img",'temp'+s[1])
          img=Image.open('temp'+s[1])
          img1=img.filter(ImageFilter.FIND_EDGES)
          img1.save('static/FIND_EDGES'+s[1])
          p='FIND_EDGES'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:          
          return render(request,'edgedetection.html')     


def latest(request):

     import datetime
     from datetime import date
     from newsapi.newsapi_client import NewsApiClient
     newsapi=NewsApiClient(api_key='8dd3a5c6aee64f1caff0a469365e86c7')
     json_data=newsapi.get_everything(q='Image tools' , language='en',
               from_param=str(date.today() - datetime.timedelta(days=29)),
               to= str(date.today()),
               page_size=24,
               page=2,
               sort_by='relevancy')
     k=json_data['articles']
     return render(request,'latestnews.html',{'k':k})  

from django.core.exceptions import ValidationError

def validate_password(password):
    
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must contain at least one digit.")
    

def about(request):
     return render(request,'aboutus.html')    

def flip(request):
     return render(request,'flip.html')

def Fliph(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          #n=int(request.POST.get('degree'))
          #print("degree",n)
          import os
          from PIL import Image
          s=os.path.splitext(f.name)
          print(s[1])

          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])
          print("img",'temp'+s[1])
          imim=img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
          imim.save('static/flip'+s[1])
          p='flip'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'fliph.html')
     

def Flipv(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          #n=int(request.POST.get('degree'))
          #print("degree",n)
          import os
          from PIL import Image
          s=os.path.splitext(f.name)
          print(s[1])

          handle_uploaded_file(f,'temp'+s[1])
          img=Image.open('temp'+s[1])
          print("img",'temp'+s[1])
          imim=img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
          imim.save('static/flip'+s[1])
          p='flip'+s[1]
          print("p")
          return render(request,'result.html',{'p':p})
     else:
          return render(request,'flipv.html')     
     

def bar(request):
     import barcode
     from barcode.writer import ImageWriter
     from django.http import HttpResponse

     if request.method == 'POST':
        barcode_data = request.POST.get('barcode_data')
        barcode_format = request.POST.get('barcode_format')

        barcode_class = barcode.get_barcode_class(barcode_format)
        barcode_image = barcode_class(barcode_data, writer=ImageWriter())
        barcode_image.save('static/barcode')
        p='barcode'
        print("p")
        return render(request,'barcode.html',{'p':p,'msg':1})
        # Create a response with the barcode image
        #response = HttpResponse(content_type='image/png')
        #barcode_image.write(response)
        #return response
     else:
        return render(request, 'barcode.html')


from qrcode import QRCode, constants
from qrcode.image import svg, pil
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render

def qrcode(request):
    if request.method == 'POST':
        qr_data = request.POST.get('qr_dat')

        qr = QRCode(
            version=1,  # QR code version (1 to 40, higher value for more complex data)
            error_correction=constants.ERROR_CORRECT_M,  # Error correction level
            box_size=10,  # Size of each box (pixel) in the QR code
            border=4,  # Size of the border (white space) around the QR code
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        #qr_image_stream = BytesIO()
        qr_image = qr.make_image(fill_color="black", back_color="white")

        qr_image.save('static/qrcode.png','PNG')
        p='qrcode'
        print("p")
        return render(request,'qrcode.html',{'p':p,'msg':1})

        
    else:
         return render(request, 'qrcode.html')


def contrast(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          val=int(request.POST.get('contrast'))
          img=Image.open('temp'+s[1])
          
          enhancer = ImageEnhance.Contrast(img)
          img1=enhancer.enhance(val)


          img1.save('static/contrast'+s[1])
          p='contrast'+s[1]
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
           return render(request,'contrast.html')


from PIL.ImageFilter import CONTOUR
def contour(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          s=os.path.splitext(f.name)
          print(f.name)
          print(s[1])
          handle_uploaded_file(f,'temp'+s[1])
          val=int(request.POST.get('contrast'))
          img=Image.open('temp'+s[1])
          
          #enhancer = ImageEnhance.Contrast(img)
          #img1=enhancer.enhance(val)
          img1 = img.filter(CONTOUR)

          img1.save('static/contour'+s[1])
          p='contour'+s[1]
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
           return render(request,'contour.html')     



from moviepy.editor import VideoFileClip

from moviepy.editor import VideoFileClip
import os

def video(request):
    if request.method == "POST":
        input_video = request.FILES['file1']
        output_gif_path = "static/out.gif"
        resize = (320, 240)
        fps = 10

        # Save the uploaded video to a temporary file
        temp_video_path = 'temp_video.mp4'  # Choose a temporary file path
        with open(temp_video_path, 'wb') as temp_video:
            for chunk in input_video.chunks():
                temp_video.write(chunk)

        clip = VideoFileClip(temp_video_path)

        if resize:
            clip = clip.resize(resize)

        if fps:
            clip = clip.set_fps(fps)

        clip.write_gif(output_gif_path)

        # Delete the temporary video file
        os.remove(temp_video_path)

        p = output_gif_path
        print(p)
        return render(request, 'vidtogif.html', {'p': p,'msg':1})
    else:
        return render(request, 'vidtogif.html')

import os
import numpy as np
import textwrap

def addtext(request):
    if not request.session.has_key('email'):
        return redirect('/Login')
    
    if request.method == "POST":
        f = request.FILES['file1']
        s = os.path.splitext(f.name)
        print(f.name)
        print(s[1])
        handle_uploaded_file(f, 'temp' + s[1])

        image = Image.open('temp' + s[1])
        font_size_percent = 15  
        image_width, image_height = image.size
        font_size = int(min(image_height, image_width) * font_size_percent / 100)
        font = ImageFont.truetype(r"C:\Users\MUSKAN SAINI\image_tool\imageapp/arial.ttf", font_size)

        # Get user input for text, position, and color
        text = request.POST.get('text1')
        x = int(request.POST.get('x'))
        y = int(request.POST.get('y'))
        color = request.POST.get('color')

        # Wrap the text to fit within 50 characters per line (adjust the width as needed)
        wrapper = textwrap.TextWrapper(width=40)
        word_list = wrapper.wrap(text=text)

        # Create img and draw object
        draw = PIL.ImageDraw.Draw(image)

        # Draw each line onto the image
        line_height = font.getbbox('hg')[1]  # Height of a line with 'h' and 'g' characters (approximation)
        y_offset = y
        for line in word_list:
            draw.text((x, y_offset), line, font=font, fill=color)
            y_offset += line_height

        image.save("static/output.png")
        p = "output.png"
        print(p)
        return render(request, 'result.html', {'p': p})
    else:
        return render(request, 'addtxt.html')

     
def png(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          
          handle_uploaded_file(f,'temp'+'.png')
          
          img=Image.open('temp'+'.png')
     

          img.save('static/pngimg'+'.png',format='PNG')
          p='pngimg'+'.png'
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
           return render(request,'jpgpng.html')
     
def jpg(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     if request.method=="POST":
          f=request.FILES['file1']
          import os
          import numpy as np
          
          handle_uploaded_file(f,'temp'+'.jpg')
          img=Image.open('temp'+'.jpg')
          rgb_image = img.convert('RGB')
          rgb_image.save('static/pngimg'+'.jpg', format='JPEG')
          
     

          #img.save('static/pngimg'+'.jpg',format='jpg')
          p='pngimg'+'.jpg'
          print("p")
          
          return render(request,'result.html',{'p':p})
     else:
         return render(request,'pngtojpg.html')   




