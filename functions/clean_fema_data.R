`%||%` <- function(x, fallback) {
  if (is.null(x) || length(x) == 0 || is.na(x)) fallback else x
}

clean_fema_data <- function(records) {
  rows <- lapply(records, function(record) {
    data.frame(
      disaster_number = as.integer(record$disasterNumber %||% NA_integer_),
      declaration_date = substr(as.character(record$declarationDate %||% ""), 1, 10),
      state = as.character(record$state %||% "Unknown"),
      declaration_type = as.character(record$declarationType %||% "Unknown"),
      incident_type = as.character(record$incidentType %||% "Unknown"),
      declaration_title = as.character(record$declarationTitle %||% "Untitled declaration"),
      incident_begin_date = substr(as.character(record$incidentBeginDate %||% ""), 1, 10),
      incident_end_date = substr(as.character(record$incidentEndDate %||% ""), 1, 10),
      designated_area = as.character(record$designatedArea %||% "Area not reported"),
      stringsAsFactors = FALSE
    )
  })

  clean <- do.call(rbind, rows)
  clean <- clean[!is.na(clean$disaster_number) & clean$declaration_date != "", ]
  clean <- clean[order(clean$declaration_date, decreasing = TRUE), ]
  rownames(clean) <- NULL
  clean
}

