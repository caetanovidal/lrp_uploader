PROJECT = "crop-warehouse"
CALCULATED_TABLE_ID = "crop-warehouse.demand_studio.calculated"
PIPELINE_TARGET_TABLE_ID = "crop-warehouse.demand_studio.pipeline_targets"
CMU_TEMPLATE_TABLE_ID = ""

CE_TABLE_ID = "crop-warehouse.non_demand_studio.CE"
MQC_TABLE_ID = "crop-warehouse.non_demand_studio.MQC"

DS_TABLES = [PIPELINE_TARGET_TABLE_ID]
NON_DS_TABLES = [CE_TABLE_ID, MQC_TABLE_ID]

COLUMNS_CE = ["Business Justification","Controlled Environment Type","Crops","Earliest Start Date","End Point",
                        "Generation","Grow Out Type","Growing Organization","Latest Start Date","Lumos ID","Material Type",
                        "Measuring System","Organization","OWNERS","Plant Production Workflow","Planting Year",
                        "Post-Propagation Cycle Time (Days)","Propagation Cycle Time (Days)","Requester","Resource Required",
                        "Tag","Trial Type","Trial Intent","Pot or Flat Type","Plants per Pot or Flat","Pot or Flat Soil Type",
                        "Pot or Flat Fertilizer Type","Pot or Flat Fertilizer Rate","Pot or Flat Irrigation Type","Bench Height",
                        "Number Planting Frequency","Planting Frequency","Number Of Plantings","Originating Country", "# of Pots", "# of Flats", "Preferred Site"]

COLUMNS_MQC = ["# of assays","ACTION NEEDED","Assay Type (MQC only)","Crops","Forecast_uploaded_by_CWID","forecastDesc",
                    "function","genoLab","Lumos ID","Planting Year","projectTypeCd","Resource Required","sampleTypeCd",
                    "scheduledLabReceivedDate","Submission_Group","Tag","Technology", "Number of Data Points", "Number of Samples"]

COLUMNS_CALCULATED = ["Demand Planning Segment", "Region", "Submarket", "Market", "Trait", 
                              "Roadmap Name", "Breeding Methodology", "Crop", "Stage", "Sequence of Operations", 
                              "Operation", "Product Concept", "Relative Start to input", "Calculated Timeline", 
                              "Time", "Year", "Month", "MonthName", "Parent Selection", "Parent Success", 
                              "Origin Selection", "Line Selection", "Origin Success", "Line Success", "Hybrid Selection", 
                              "Hybrid Success", "Resource Conversion Factor", "Seed Products Conversion Factor", 
                              "Calculated Parents", "Calculated Origins", "Calculated Lines", "Calculated Hybrids", 
                              "Calculated Cost", "Calculated Seed Products", "Calculated Resources", "SEED_PLOTS", 
                              "SEED_SRE", "Resource Required", "Plot Row Length Uom", "Reps/Site", 
                              "Number Of Bayer Growing Sites", "Plot Row Length", "Rows Per Plot", "Velocity Location", 
                              "Conversion Unit", "Pipeline Percentage", "SREeq", "#Rows/entry", "Check Factor",
                              "Trial Type", "Trial Intent", "Material Type", "Planting Material Stage", 
                              "Maturity Min", "Maturity Max", "Cycle Time (Days)", "Compliance Types", "Harvest Type", 
                              "Number Of Non-Bayer Growing Sites", "Measuring System", "Row Spacing", "Row Spacing Uom", 
                              "Generation", "Cross Type", "Pollination Layout", "AR", "Tag", "notes", "value_origin_ind_cc", 
                              "value_origin_cc", "value_origin_ind", "value_origin", "value_org_line_ind", "value_org_line", 
                              "Field Test Year", "#Testers", "Season", "Global Hub", "Requesting Organization",
                              "Originating Country", "treatments"] 
 

COLUMNS_PIPELINE_TARGET = ['Demand Planning Segment', 'Crop', 'Region', 'Market', 'Submarket', 'Trait', 'Product Concept', 
                'Field Test Year', 'Stage', 'Breeding Methodology', 'Roadmap Name', 'Target Origins', 'Target Lines',
                'Target Hybrids', 'Ideal Plant Month', 'Ideal Plant Day', 'Global Hub', 'Originating Country', 
                'Requesting Organization', 'Target Parents']
                
COLUMNS_CMU_TEMPLATE = ["Request #", "Compliance Types", "Crops", "Cross Type", "Cycle Time (Days)", "Description", "Earliest Start Date", "Global Hub",
                "Harvest Type", "How do you want to capture Plot Dimensions?", "Lumos ID", "Market", "Material Type", "Maturity", "Measuring System", "Name", "Non-Seed Product Treatments", 
                "Number Of Bayer Growing Sites", "Number Of Non-Bayer Growing Sites", "Owners", "Planting Material Stage", "Planting Year", "Plot Row Length", "Plot Row Length Uom", 
                "Pollination Layout", "Reps / Site", "Requested ICB Male", "Requester", "Requesting Organization", "Row Spacing", "Row Spacing Uom", "Rows Per Plot", "Season", "Seed Products",
                "Sub-Market", "Tags", "Trial Intent", "Trial Type", "Generation", "Owner Groups", "Growing Organization", "Originating Country", "Homesite", "Footprint Area Uom", "Total Area Uom",
                "Footprint #", "Environment Name", "Comments"]
