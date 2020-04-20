from __future__ import print_function, absolute_import
import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

import logging

logging.basicConfig(level=logging.INFO)


def find_wineries(line, term):
    if term in line:
        yield line

PROJECT = "single-patrol-273415"
BUCKET = "print-lake-bucket"

def run():
    import time
    gcs_path = "gs://{0}/dataflow".format(BUCKET)
    pipeline =  beam.Pipeline(runner="DataflowRunner", argv=[
        "--project", PROJECT,
        "--staging_location", ("%s/staging_location" % gcs_path),
        "--temp_location", ("%s/temp" % gcs_path),
        "--output", ("%s/output" % gcs_path),
        "--setup_file", "./setup.py"
    ])

    input_file = 'dataflow_pipeline/spikey_sales_weekly.csv'
    output_prefix = 'gs://{0}/output/'.format(BUCKET)

    search_term = 'California'

    logging.info('Pre-pipeline')
    (pipeline
        | "GetWineries" >> beam.io.ReadFromText(input_file)
        | 'GrepWineriesInCalifornia' >> beam.FlatMap(lambda line: find_wineries(line,search_term))
        | "WriteToFile" >> beam.io.WriteToText(output_prefix)
    )
    pipeline.run()
