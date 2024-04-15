$zip_files = Get-ChildItem -Path "./data" -Filter "*.zip"

foreach ($zip_file in $zip_files) {
    $zip_file_name = $zip_file.Name
    $zip_file_name_no_extension = $zip_file_name -replace ".zip", ""
    $zip_file_path = $zip_file.FullName
    $unzip_folder_path = "./data/$zip_file_name_no_extension"

    Write-Host "Unzipping $zip_file_name to $unzip_folder_path"

    Expand-Archive -Path $zip_file_path -DestinationPath $unzip_folder_path
}
