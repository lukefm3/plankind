# PlanKind public demonstration pipeline
# FEMA OpenFEMA - Disaster Declarations Summaries

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Package 'jsonlite' is required.")
}

source(file.path("functions", "clean_fema_data.R"))

source_url <- paste0(
  "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries",
  "?$orderby=declarationDate%20desc&$top=5000"
)

processed_dir <- "processed_data"
website_data_dir <- file.path("website", "data")
dir.create(processed_dir, recursive = TRUE, showWarnings = FALSE)
dir.create(website_data_dir, recursive = TRUE, showWarnings = FALSE)

message("Downloading recent FEMA disaster declarations...")
payload <- jsonlite::fromJSON(source_url, simplifyVector = FALSE)
records <- payload$DisasterDeclarationsSummaries
if (is.null(records) || !is.list(records)) {
  stop("OpenFEMA response did not contain the expected records.")
}

clean <- clean_fema_data(records)
if (nrow(clean) < 1) stop("Validation failed: no usable declarations.")
if (any(nchar(clean$state) != 2)) stop("Validation failed: unexpected state code.")
if (any(is.na(as.Date(clean$declaration_date)))) stop("Validation failed: invalid declaration date.")

cutoff <- Sys.Date() - 730
recent <- clean[as.Date(clean$declaration_date) >= cutoff, ]
if (nrow(recent) < 1) stop("Validation failed: no declarations within the last two years.")

write.csv(recent, file.path(processed_dir, "fema_declarations.csv"), row.names = FALSE, na = "")
write.csv(recent, file.path(website_data_dir, "fema_declarations.csv"), row.names = FALSE, na = "")

metadata <- list(
  generated_at_utc = format(Sys.time(), "%Y-%m-%dT%H:%M:%SZ", tz = "UTC"),
  source_name = "FEMA OpenFEMA - Disaster Declarations Summaries",
  source_url = source_url,
  record_count = nrow(recent),
  coverage_start = min(recent$declaration_date),
  coverage_end = max(recent$declaration_date)
)
jsonlite::write_json(metadata, file.path(processed_dir, "metadata.json"), auto_unbox = TRUE, pretty = TRUE)
jsonlite::write_json(metadata, file.path(website_data_dir, "metadata.json"), auto_unbox = TRUE, pretty = TRUE)
message(sprintf("Published %s validated declaration records.", nrow(recent)))

