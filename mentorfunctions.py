import samplecode

updated_record=None
record_number=None
succuss="No"
mentee_records_list=samplecode.mentee_details_tree.inorder()
# print(mentee_records_list)
def update(tree,Sno,newdetail,index):
    global updated_record
    global record_number
    global mentee_records_list
    global success

    if int(tree.key[0])==Sno:
        #print(len(mentee_records_list))
        mentee_records_list[int(Sno-1)][index]=newdetail
        success="Yes"
    elif Sno<int(tree.key[0]):
        if tree.lchild:
            update(tree.lchild,Sno,newdetail,index)
        else:
            return False
    elif Sno>int(tree.key[0]):
        if tree.rchild:
            update(tree.rchild,Sno,newdetail,index)
        else:
            return False


Type=input("Which detail you want to edit:")

"""Digital ID,Register Number,Student Name,Section,Department"""
if Type.lower()=="digital id" or Type=="Digital ID":
    Sno=int(input("Enter serial number: "))
    column=1
    new=int(input("Enter new digital ID:"))
    update(samplecode.mentee_details_tree,Sno,new,column)
    if success=="Yes":
        samplecode.mentee_details_tree=samplecode.createBST(mentee_records_list)
        print(samplecode.mentee_details_tree.inorder())
    else:
        print("Entered serial number is invalid.")

elif Type.lower()=="register number" or Type=="Register Number":
    Sno=int(input("Enter serial number: "))
    column=2
    new=int(input("Enter new register number:"))
    update(samplecode.mentee_details_tree,Sno,new,column)
    if success=="Yes":
        samplecode.mentee_details_tree=samplecode.createBST(mentee_records_list)
    else:
        print("Entered serial number is invalid.")

elif Type.lower()=="student name" or Type=="Student Name":
    Sno=int(input("Enter serial number: "))
    column=3
    new=int(input("Enter new Student Name:"))
    update(samplecode.mentee_details_tree,Sno,new,column)
    if success=="Yes":
        samplecode.mentee_details_tree=samplecode.createBST(mentee_records_list)
    else:
        print("Entered serial number is invalid.")

elif Type.lower()=="section" or Type=="Section":
    Sno=int(input("Enter serial number: "))
    column=4
    new=int(input("Enter new Section:"))
    update(samplecode.mentee_details_tree,Sno,new,column)
    if success=="Yes":
        samplecode.mentee_details_tree=samplecode.createBST(mentee_records_list)
    else:
        print("Entered serial number is invalid.")

elif Type.lower()=="department" or Type=="Department":
    Sno=int(input("Enter serial number: "))
    column=5
    new=int(input("Enter new Department:"))
    update(samplecode.mentee_details_tree,Sno,new,column)
    if success=="Yes":
        samplecode.mentee_details_tree=samplecode.createBST(mentee_records_list)
    else:
        print("Entered serial number is invalid.")

else:
    print("You can't change S.no, digital Id and gender")




    