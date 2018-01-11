#simple bash script to collect the data to be averaged for the critical temperature curve

./Criticaltemp.py
mv data.py data1.py

./Criticaltemp.py
mv data.py data2.py

./Criticaltemp.py
mv data.py data3.py

./Criticaltemp.py
mv data.py data4.py

./Criticaltemp.py
mv data.py data5.py

cat data1.py >> data2.py
rm data1.py
cat data2.py >> data3.py
rm data2.py
cat data3.py >> data4.py
rm data3.py
cat data4.py >> data5.py
rm data4.py

mv data5.py average_lists.py

