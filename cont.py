import google.generativeai as genai
import requests
import PyPDF2
import pdf
import time

genai.configure(api_key="USE google api key")



def send_content(message):
    generation_config = {
        "temperature": 0.8,
        "top_k": 60,
        "top_p": 0.9,
        "max_output_tokens": 300,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            generation_config=generation_config,
        )
    chat_session = model.start_chat(
            history=[]
        )
    response = chat_session.send_message(f"""Analyze the outline and write done topics are included:
    {message}
    i just need topics not anything else follow it strictly. don't write the heading of  "topics included" also ingonre to write any information attendance and 
    presentation and don't write the name of books.just write topics not anything else in berifly.they should be short and simple.""")
    
    return response.text
    # for i in nlist:
            
    #         print(i)
    
    
def engine(topic,model):
    generation_config = {
        "temperature": 0.8,
        "top_k": 60,
        "top_p": 0.9,
        "max_output_tokens": 1000,
        "response_mime_type": "text/plain",
    }
    model = genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config,

        )

    chat_session = model.start_chat(
            history=[]
        )
    response = chat_session.send_message(f"""i want you make notes of the topic of : {topic} 
                                         On what i am giving to you make full details notes so i can cover my university outline and make it simple and easy language.and dont miss any detail""")
    
    return response.text
    
def note(pdf_file):
    ext_text=""
    models=["",'models/gemini-1.5-pro','models/gemini-1.5-flash','models/gemini-2.0-flash','models/gemini-1.5-flash']
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        extracted_text=""
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text1 = page.extract_text()   
            text2 = send_content(text1)
            send_content(text2)

            extracted_text += text2 + "\n\n"
            time.sleep(3)
            # print(extracted_text)
        list1=[line.strip() for line in extracted_text.split("\n") if line.strip()]
        nlist=list(list1)
        for i in nlist:
            print(i)
        mod=0
        for p in range(0,len(nlist)-1):
            if(mod==4):
                mod=1
            if(p%5==0):
                mod=mod+1
                text3=engine(nlist[p],models[mod])
                print(mod," ",p)
                # print (text3,p)
            else:
                text3=engine(nlist[p],models[mod])
                print(mod," ",p)
                # print (text3,p)
            if text3:
                ext_text+=text3+"\n\n"
            time.sleep(5)
        # print(ext_text)
    pdf.pdf1(ext_text)
note(r"Write down the path of the pdf file or course outline")

















