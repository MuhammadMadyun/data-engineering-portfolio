#### Phase 1: Step 1A - Data Acquisition
### Primary Dataset: 
## Diabetes 130-US Hospitals	   -     Contains readmission records for diabetic patients. 

# UC Irvine Machine Learning Repository 

import ucimlrepo as uc
# fetch dataset 
diabetes_130_us_hospitals_for_years_1999_2008 = uc.fetch_ucirepo(id=296) 

# fetch dataset 
cdc_diabetes_health_indicators = uc.fetch_ucirepo(id=891) 
  
  
# data (as pandas dataframes) 
a = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
b = diabetes_130_us_hospitals_for_years_1999_2008.data.targets 

# data (as pandas dataframes) 
c = cdc_diabetes_health_indicators.data.features 
d = cdc_diabetes_health_indicators.data.targets 
  
# metadata 
print(diabetes_130_us_hospitals_for_years_1999_2008.metadata) 
# metadata 
print(cdc_diabetes_health_indicators.metadata) 
  
# variable information 
print(diabetes_130_us_hospitals_for_years_1999_2008.variables) 
  
# variable information 
print(cdc_diabetes_health_indicators.variables) 
