1. make all
2. cd dist
3. spark-submit --deploy-mode client --py-files jobs.zip main.py --job_name reconciler --environment qa --region us-east-1 --in_path s3://bucket
4. spark-submit --deploy-mode client --py-files jobs.zip main.py
5. spark-submit --deploy-mode client --py-files jobs.zip main.py --job_name reconciler --environment qa

