# Custom Library 
### To validate a transaction data with different formate , e.g: JSON , XML .
self.data indicate to the loaded data from any file **[JSON , XML]**, and the struct of this data is same in after reading any file 

* To run code using terminal : 
```
python main.py filepath/[transactionfile]

```
* To run code using docker need to build docker image and run it :
```
sudo docker build -t check-trans .
sudo docker run -t check-trans tranaction.xml 
```
OR using docker volume to test other files:
```
sudo docker run -t -v /home/transaction2.json:/transaction2.json check-trans /transaction2.json

```

** Note:
- [x] provide the transaction file in same directory of main.py to copy it inside the container before build docker-image
- [x] Provide transaction filename with command [docker run] 
- [ ] using docker volume to link file from outside container





