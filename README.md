# Data for modeling pallet logistics with Colab
This code could be creating an archive with twelve excel files. Files simulate monthly sales activity.
1. Run GenDataFiles.py
2. Create folder and moving generated files:
    
    !mkdir ./SalesData
    
    !mv ./*.csv ./SalesData
3. Run ArchivationCreatedFiles.py
4. Run MergeAndCleanDate.py
5. Run AddFeature.py
