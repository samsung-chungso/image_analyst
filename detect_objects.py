import arcpy
arcpy.ImportToolbox(r"@\Image Analyst Tools.tbx")
with arcpy.EnvManager(extent='126.938797778772 37.5590594680161 126.952584966152 37.5687028959543 GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=1, processorType="CPU", scratchWorkspace=r""):
    arcpy.ia.DetectObjectsUsingDeepLearning(
        in_raster="영상",
        out_detected_objects=r"C:\Users\Geocontents\Documents\ArcGIS\Projects\Road Extraction\Default.gdb\ewha_road_NMS",
        in_model_definition=r"C:\Users\Geocontents\Downloads\RoadExtraction_Global.dlpk",
        arguments="batch_size 4",
        run_nms="NMS",
        confidence_score_field="Confidence",
        class_value_field="Class",
        max_overlap_ratio=0,
        processing_mode="PROCESS_AS_MOSAICKED_IMAGE"
    )