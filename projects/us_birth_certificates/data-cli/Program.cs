// Copyright (c) Frank Buckley and Contributors. All Rights Reserved.
// Frank Buckley and Contributors licence this file to you under the MIT license.

namespace Populations.Data.CLI;

public static class Program
{
    public static async Task<int> Main()
    {
        var database = new Database("../../../../data/births.ddb");

        await database.CreateDatabaseAsync().ConfigureAwait(false);

        using var stream = File.OpenRead("../../../../data/Nat2023us/Nat2023PublicUS.c20240509.r20240724.txt");
        using var reader = new StreamReader(stream);

        for (var i = 0; i < 50; i++)
        {
            var cols = await reader.ReadLineAsync().ConfigureAwait(false);

            if (!string.IsNullOrWhiteSpace(cols))
            {
                var row = DataRow.Read(cols);
                Console.WriteLine(row);
            }
        }

        return 0;
    }
}
