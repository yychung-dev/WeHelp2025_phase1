print("=== Task 1 ===")
def find_and_print(messages, current_station):
    import re
    all_station =['Songshan','Nanjing Sanmin','Taipei Arena','Nanjing Fuxing','Songjiang Nanjing','Zhongshan','Beimen','Ximen','Xiaonanmen','Chiang Kai-Shek Memorial Hall','Guting','Taipower Building','Gongguan','Wanlong','Jingmei','Dapinglin','Qizhang','Xiaobitan','Xindian City Hall','Xindian']
    all_but_branch =['Songshan','Nanjing Sanmin','Taipei Arena','Nanjing Fuxing','Songjiang Nanjing','Zhongshan','Beimen','Ximen','Xiaonanmen','Chiang Kai-Shek Memorial Hall','Guting','Taipower Building','Gongguan','Wanlong','Jingmei','Dapinglin','Qizhang','Xindian City Hall','Xindian']
    all_sub1 =['Songshan','Nanjing Sanmin','Taipei Arena','Nanjing Fuxing','Songjiang Nanjing','Zhongshan','Beimen','Ximen','Xiaonanmen','Chiang Kai-Shek Memorial Hall','Guting','Taipower Building','Gongguan','Wanlong','Jingmei','Dapinglin','Qizhang','Xiaobitan']
    all_sub2 =['Xiaobitan','Qizhang','Xindian City Hall','Xindian']
    if current_station not in all_station:          
        print ('Current station '+current_station+ ' is not in green line.')
        return
    friend_name = list(messages.keys())
    friend_say = list(messages.values())
    friend_station=[]
    distance = []
    for i in range (0,len(friend_say)): 
        not_in_line = 'yes'
        for j in range(0,len(all_station)):
            role = re.compile(all_station[j])
            if role.search(friend_say[i]) != None:
                friend_station.insert(i,all_station[j])
                not_in_line='no'
                break
        if not_in_line == 'yes':   
            friend_station.insert(i,'not in green line')  
    for k in range(0,len(friend_station)):
        if current_station in all_but_branch and friend_station[k] in all_but_branch:
            distance.insert(k,abs(all_but_branch.index(current_station) - all_but_branch.index(friend_station[k])))
        else:
            if current_station in all_sub1 and friend_station[k] in all_sub1:
                 distance.insert(k,abs(all_sub1.index(current_station) - all_sub1.index(friend_station[k])))
            else:
                if friend_station[k] == 'not in green line':   
                   distance.insert(k,99999)       
                else:
                   distance.insert(k,abs(all_sub2.index(current_station) - all_sub2.index(friend_station[k])))
        
    print(friend_name[distance.index(min(distance))]) 
messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}

find_and_print(messages,"Wanlong")
find_and_print(messages,"Songshan")
find_and_print(messages,"Qizhang")
find_and_print(messages,"Ximen")
find_and_print(messages,"Xindian City Hall")


print("=== Task 2 ===")
john_arr =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
bob_arr =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
jenny_arr =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

def count_time(hour, duration):
    import re
    result = []
    for i in range (0,duration):
        result.insert(i,hour+i)
    return result

def choose_consultant(consultants, criteria):
    import re
    if criteria=="price":
       return sorted( consultants, key = lambda x : x['price'] )[0]['name']
    else:
       return sorted( consultants, key = lambda x : x['rate'], reverse=True )[0]['name']

def book (consultants, hour, duration, criteria) : 
    import re
    global john_arr
    global bob_arr
    global jenny_arr
    found=False
    targtime_arr = count_time(hour, duration)
    while len(consultants) > 0:
        targ_consultant = choose_consultant(consultants, criteria)
        if targ_consultant=="John":  
            if set(targtime_arr).issubset(john_arr):
                john_arr=[item for item in john_arr if item not in targtime_arr]
                print("John")
                found=True
                break
            else:
                consultants=[item for item in consultants if item not in [{"name":"John", "rate":4.5, "price":1000}]]  
        elif targ_consultant=="Bob":
            if set(targtime_arr).issubset(bob_arr):
                bob_arr=[item for item in bob_arr if item not in targtime_arr]
                print("Bob")
                found=True
                break
            else:
                consultants=[item for item in consultants if item not in [{"name":"Bob", "rate":3, "price":1200}]]                
        elif targ_consultant=="Jenny":           
            if set(targtime_arr).issubset(jenny_arr):                               
                jenny_arr=[item for item in jenny_arr if item not in targtime_arr]
                print("Jenny")
                found=True
                break
            else:                
                consultants=[item for item in consultants if item not in [{"name":"Jenny", "rate":3.8, "price":800}]]  

    if not(found):
        print("No Service")

consultants=[
   {"name":"John", "rate":4.5, "price":1000},
   {"name":"Bob", "rate":3, "price":1200},
   {"name":"Jenny", "rate":3.8, "price":800}
]
book(consultants,15,1,"price") 
book(consultants,11,2,"price")
book(consultants,10,2,"price")
book(consultants,20,2,"rate")
book(consultants,11,1,"rate")
book(consultants,11,2,"rate")
book(consultants,14,3,"price")


print("=== Task 3 ===")
def pick_midname(fullname):
            midname=''
            if len(fullname) == 2:
                midname = fullname[1]
            elif len(fullname) == 3:
                midname = fullname[1]
            elif len(fullname) == 4:
                midname = fullname[2]
            elif len(fullname) == 5:
                midname = fullname[2]
            return midname          

def func(*data):  
    unique_list=''       
    for i in range(0,len(data)):
        unique_flag=1  
        name1=pick_midname(data[i])
        for j in range(0,len(data)):
            if i!=j:
                name2=pick_midname(data[j])
                if name1==name2:
                    unique_flag=0
                    break     
        if unique_flag==1:
            unique_list=unique_list+''+data[i]
    if unique_list=='':
        unique_list='沒有'
    print(unique_list)

func("彭大牆","陳王明雅","吳明")
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")
func("郭宣雅", "夏曼藍波安", "郭宣恆")


print("=== Task 4 ===")
def get_number(index):
    number = 0
    x=[4,4,-1]
    x_total = 0 
    ln=len(x)   
    for i in range(0,ln):
        x_total=x_total+x[i] 
 
    div_value = divmod(index,3)

    number = number + x_total * div_value[0]

    for i in range(0,div_value[1]):
        number=number+x[i]
    
    print(number)

get_number(1) 
get_number(5) 
get_number(10)
get_number(30) 