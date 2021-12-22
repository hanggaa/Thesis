# Load the ggplot2 package which provides
# the 'mpg' dataset.
library(shiny)
library(ggplot2)
library(gsheet)

ui <- fluidPage(
  titlePanel("Basic DataTable"),
  # Create a new row for the table.
  DT::dataTableOutput("table")
)

server <- function(input, output) {
  
  # Filter data based on selections
  output$table <- DT::renderDataTable(DT::datatable({
    url <- 'https://docs.google.com/spreadsheets/d/1hyu6w25TcyzN8DGUmW-kwSx73mWYUIyUYY-Ivpmsk2k/edit?usp=sharing'
    data <- gsheet2tbl(url)
    data
  }))
  
}

shinyApp(ui, server)