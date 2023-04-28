import random
rows, cols = (6, 6)
list_A=[['JFBG','GFJV','HJU','GDH','HUD','UDG'],['EGHY','JAU','YRD','TOH','IWB','ITH'],
['XYZ','WER','RHF','DHU','IXV','HUS'],['EBK','SJI','IDG','ESX','HDI','VXJ'],['JWF','GDU','BXJ','ZSC','ISS','BJZ'],
['WE','DHS','HFU','IGS','JDU','IHD']]
list_B=random.sample(list_A,3)  
print(list_B)
l=[]        
for i in range(0,3):  
     l.append(random.choice(list_B[i]))   
    
print(l)       
    


