# Data for modeling pallet logistics with Colab
This code could be creating an archive with twelve excel files. Files simulate monthly sales activity.
1. %load_ext autoreload

   %autoreload 2
   
2. %run GenDataFiles.py

3. Create folder and moving generated files:
    
    !mkdir ./SalesData
    
    !mv ./*.csv ./SalesData
    
4. %run ArchivationCreatedFiles.py
   
   !ls -GFlash --color ./
5. %run MergeAndCleanDate.py
   
   df
6. %run AddFeature.py

   df
