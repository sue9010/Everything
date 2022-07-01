import os
import shutil

src = "//cox_biz/business/2022"+"/"
dir_PR = r"\\cox_biz\business\2022\3-판매\3-출고요청서"
dir_QT = r"\\cox_biz\business\2022\3-판매\0-견적서(Quotation)"
dir_PI = r"\\cox_biz\business\2022\3-판매\2-Profoma invoice"
dir_PO = r"\\cox_biz\business\2022\4-구매\1-발주서(PO)"
dir_T = r"\\cox_biz\business\2022\3-판매\5-납품확인서,거래명세서"
dir_RMA = r"\\cox_biz\business\2022\7-RMA\0-RMA form, RMA 요청서"

file_list = os.listdir(r"\\cox_biz\business\2022"+"/") #폴더의 파일명을 리스트화 

for file in file_list: 
    temp_list = file.split("_") #파일명중 "_"로 분리하여 리스트화 
    if temp_list[0] == '출고요청서' or temp_list[0]=='LD' or temp_list[0]=='선대체 요청서': 
        shutil.move(src+file, dir_PR+"/"+file)
    elif temp_list[0] == 'Quotation'or temp_list[0]=='견적서':
        shutil.move(src+file, dir_QT+"/"+file)
    elif temp_list[0] == 'PI':
        shutil.move(src+file, dir_PI+"/"+file)  
    elif temp_list[0] == 'PO':
        shutil.move(src+file, dir_PO+"/"+file)
    elif temp_list[0] == '거래명세서' or temp_list[0]=='납품확인서':
        shutil.move(src+file, dir_T+"/"+file)
    elif temp_list[0] == 'RMA 요청서' or temp_list[0]=='RMA form' or temp_list[0]=='회수내역서':
            shutil.move(src+file, dir_RMA+"/"+file) 



file_sort = ['기안서','출고요청서','LD','거래명세서','납품확인서','QT','PI','PO','RMA 요청서','RMA form','선대체 요청서']