// Copyright (c) Frank Buckley and Contributors. All Rights Reserved.
// Frank Buckley and Contributors licence this file to you under the MIT license.

using DuckDB.NET.Data;

namespace Populations.Data.CLI;

public class Database
{
    public Database(string path)
    {
        Path = path;
    }

    public string Path { get; }

#pragma warning disable CA2007 // Consider calling ConfigureAwait on the awaited task
    public async Task CreateDatabaseAsync()
    {
        if (File.Exists(Path))
        {
            File.Delete(Path);
        }

        await using var connection = new DuckDBConnection($"Data Source={Path}");

        await connection.OpenAsync().ConfigureAwait(false);

        await using var command = connection.CreateCommand();

        command.CommandText = """
            CREATE TABLE births
            (
                dob_yy INTEGER,
                dob_mm INTEGER,
                bfacil INTEGER,
                f_bfacil INTEGER,
                mage_impflg INTEGER,
                mage_repflg INTEGER,
                mager INTEGER,
            );
            """;

        _ = await command.ExecuteNonQueryAsync().ConfigureAwait(false);
    }
}
