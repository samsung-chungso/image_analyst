import arcpy
arcpy.ImportToolbox(r"@\Image Analyst Tools.tbx")
with arcpy.EnvManager(extent='126.93796490671 37.5552238205234 126.959007382069 37.5699419489681 GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=1, processorType="CPU", scratchWorkspace=r""):
    arcpy.ia.DetectObjectsUsingDeepLearning(
        in_raster="영상",
        out_detected_objects=r"C:\Users\Geocontents\Documents\ArcGIS\Projects\Road Extraction\Default.gdb\ewha_road",
        in_model_definition=r"C:\Users\Geocontents\Downloads\RoadExtraction_Global.dlpk",
        arguments="batch_size 4",
        run_nms="NO_NMS",
        confidence_score_field="Confidence",
        class_value_field="Class",
        max_overlap_ratio=0,
        processing_mode="PROCESS_AS_MOSAICKED_IMAGE"
    )