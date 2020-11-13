# <img src="./eslearn/logo/logo-lower.jpg" width = "200" height = "60" div align=left />  <font size=10>Make machine learning easy!</font>  

Easylearn is designed for machine learning mainly in resting-state fMRI, radiomics and other fields (such as EEG). Easylearn is built on top of scikit-learn, pytorch and other packages. Easylearn can assist doctors and researchers who have limited coding experience to easily realize machine learning, e.g., (MR/CT/PET/EEG)imaging-marker- or other biomarker-based disease diagnosis and prediction, treatment response prediction, disease subtyping, dimensional decoding for transdiagnostic psychiatric diseases or other diseases, disease mechanism exploration and etc.  

We focus on machine learning rather than data preprocessing. Many software, such as SPM, GRETNA, DPABI, REST, RESTPlus, CCS, FSL, Freesufer, nipy, nipype, nibabel, fmriprep and etc, can be used for data preprocessing.  

# Citing information:
If you think this software (or some function) is useful, citing the easylearn software in your paper or code would be greatly appreciated!
Citing link: https://github.com/lichao312214129/easylearn 

# Install  
```
pip install eslearn
```

# Usage
```
from eslearn import app
app.run()
```

# GUI preview
#### Main Interface
![Main Window](./eslearn/img/GUI_main.png)  
#### <center> Data loading Interface </center>
![Data loading](./eslearn/img/GUI_data_loading.png)    
#### <center> Feature engineering Interface (feature preprocessing) </center>
![Featur engineering](./eslearn/img/preprocessing.png)   
#### <center> Feature engineering Interface (dimension reduction) </center>
![Featur engineering](./eslearn/img/dimreduction.png)   
#### <center> Feature engineering Interface (feature selection) </center>
![Featur engineering](./eslearn/img/feature_selection.png)   
#### <center> Feature engineering Interface (unbalance treatment) </center>
![Featur engineering](./eslearn/img/unbalance_treatment.png) 
#### <center> Machine learning Interface </center>
![Machine learning](./eslearn/img/machine_learning.png) 

# Core Dependencies 

- sklearn
- numpy
- pandas
- openpyxl
- python-dateutil
- pytz
- scikit-learn
- scipy
- six
- nibabel
- imbalanced-learn
- skrebate
- matplotlib

# Development    
We hope you can join us!   
> Email: lichao19870617@gmail.com  
> Wechat: 13591648206  

# Supervisors/Consultants 

##### Ke Xu
    kexu@vip.sina.com  
    Brain Function Research Section, The First Affiliated Hospital of China Medical University, Shenyang, Liaoning, PR China.  
    Department of Radiology, The First Affiliated Hospital of China Medical University.

##### Yanqing Tang  
    yanqingtang@163.com  
    1 Brain Function Research Section, The First Affiliated Hospital of China Medical
    University, Shenyang, Liaoning, PR China.  
    2 Department of Psychiatry, The First Affiliated Hospital of China Medical University,
    Shenyang, Liaoning, PR China.        
    
##### Yong He  
    yong.he@bnu.edu.cn  
    1 National Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University, Beijing 100875, China  
    2 Beijing Key Laboratory of Brain Imaging and Connectomics, Beijing Normal University, Beijing 100875, China  
    3 IDG/McGovern Institute for Brain Research, Beijing Normal University, Beijing 100875, China 

# Maintainers
##### Chao Li
    lichao19870617@gmail.com
    Brain Function Research Section, The First Affiliated Hospital of China Medical University, Shenyang, Liaoning, PR China.  
    
##### Mengshi Dong
    dongmengshi1990@163.com  
    Department of Radiology, The First Affiliated Hospital of China Medical University, Shenyang, Liaoning, PR China.  

<br> <br />
If the program runs successfully, some results file will be generated under the results folder (path_out), as follows:
#### <center> Classification performances </center>
![Classification performances](./eslearn/img/classification_performances.png)  
<br> <br />

![wei](./eslearn/img/perf.png)  
<br> <br />
#### <center>Classfication weights (top 1%, BrainNet Viewer) </center>
![Top classfication weights](./eslearn/img/wei.jpg) 
<br> <br />

