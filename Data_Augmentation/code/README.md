# Note  
In the code folder, you can perform data augmentation for four datasets NYT, NYT_star, WebNLG, WebNLG_star, and the code is executed as follows:

##### Before that you need to configure your environment according to ./Similarity_match_framework/README.md.
Data augmentation on NYT dataset:
    1. python data_decomposition_NYT.py
    2. python similarity_match_NYT.py
    3. python data_augmentation_NYT.py
    4. python get_data_NYT.py

Data augmentation on NYT_star dataset:
    1. python data_decomposition_NYT_star.py
    2. python similarity_match_NYT_star.py
    3. python data_augmentation_NYT_star.py
    4. python get_data_NYT_star.py

Data augmentation on WebNLG dataset:
    1. python data_decomposition_WebNLG.py
    2. python similarity_match_WebNLG.py
    3. python data_augmentation_WebNLG.py
    4. python get_data_WebNLG.py

Data augmentation on WebNLG_star dataset:
    1. python data_decomposition_WebNLG_star.py
    2. python similarity_match_WebNLG_star.py
    3. python data_augmentation_WebNLG_star.py
    4. python get_data_WebNLG_star.py

After performing these steps, you will be in ./data folder, these are the NYT_augmentation, NYT_star_augmentation, WebNLG_augmentation, WebNLG_star_augmentation files for the augmented data.
