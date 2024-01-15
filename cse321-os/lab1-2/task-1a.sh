# 1. Create 4 files named yourID_1.txt, yourID_2.txt, yourID_3, yourID_4.txt 
# 2. 2 directories named YourName1, YourName2.
# 3. Move yourID_1.txt, yourID_2.txt, yourID_3.txt in YourName1 directory.
# 4. Copy yourID_1.txt, yourID_2.txt YourName2 directory.
# 5. Create another directory YourName3.
# 6. Now, copy the YourName1 directory along with contents to the YourName3 directory.
# 7. Now go into the YourName3 directory and check the permissions of the files/directory in there 
# 8. and change the permissions for both group and others to only read-execute for all the files.
# 9. Now go back one directory and print all the directories and files in the current working directory.
# 10. Finally, move the YourName3 folder to the root directory 
# 11. and delete the rest of the files and folders in the current working directory.
# >> Write down all the commands in the exact same order as you have written in the command line while following the instructions.
touch 20301239_1.txt 20301239_2.txt 20301239_3.txt 20301239_4.txt
mkdir Asim1 Asim2
mv 20301239_1.txt 20301239_2.txt 20301239_3.txt Asim1
cp Asim1/20301239_1.txt Asim1/20301239_2.txt Asim2
mkdir Asim3
cp -r Asim1  Asim1/* Asim3
cd Asim3
ls -lah
chmod o=rx,g=rx *
cd ..
ls .
sudo mv Asim3 /
rm -rf  *
