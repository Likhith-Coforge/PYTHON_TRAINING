acc_info = (101,'ABC','Bank_Name','IFSC_CODE',1000)
transfer_amount = int(input("Enter the amount to be transferred(<1000): "))
# user want to transfer some amount to someone, change his balance in the tuple accordingly.
acc_info = (acc_info[0],acc_info[1],acc_info[2],acc_info[3],acc_info[4]-transfer_amount)
print(acc_info)