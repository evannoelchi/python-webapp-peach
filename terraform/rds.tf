resource "aws_db_instance" "rds_instance" {
    allocated_storage = 20
    identifier = "rds-db"
    storage_type = "gp2"
    engine = "postgres"
    engine_version = "13.7"
    instance_class = "db.t3.micro"
    name = "flaskdb"
    username = "postgres"
    password = "postgres"
    publicly_accessible    = true
    skip_final_snapshot    = true


    tags = {
        Name = "RDSServerInstance"
    }
}