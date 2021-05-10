#base image 
FROM python 
COPY . /ass1
WORKDIR /ass1 
CMD python project.py