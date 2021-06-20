import pandas as pd
import numpy as np
from pathlib import Path


def prepared_data():
    current_dir = Path(__file__).absolute().parent
    df = pd.read_csv(
        current_dir / "../data/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_2446153.csv", skiprows=4
    )

    countrylist = [
        "United States",
        "China",
        "Japan",
        "Germany",
        "United Kingdom",
        "India",
        "France",
        "Brazil",
        "Italy",
        "Canada",
    ]
    df = df[df["Country Name"].isin(countrylist)]

    cols = df.columns[-12:-2]
    df.columns[0]
    cols = list(cols.insert(0, df.columns[0]))
    df_new = df[cols]

    new_df = {"Country Name": [], "year": [], "prp_rural_pop": []}

    for c in df_new["Country Name"]:
        prp_rural_pop = np.squeeze(df_new[df_new["Country Name"] == c][cols[1:]].values)
        new_df["Country Name"].extend([c] * len(prp_rural_pop))
        new_df["year"].extend(cols[1:])
        new_df["prp_rural_pop"].extend(prp_rural_pop)

    df_new = pd.DataFrame(new_df)

    df = df[["Country Name", "2000", "2019"]]
    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars="Country Name", value_vars=["2000", "2019"])
    df_melt.columns = ["country", "year", "variable"]
    df_melt["year"] = df_melt["year"].astype("datetime64[ns]").dt.year

    # add column names
    df_melt.columns = ["country", "year", "percentrural"]

    # prepare data into x, y lists for plotting
    df_melt.sort_values("percentrural", ascending=False, inplace=True)

    data = []
    for country in countrylist:
        x_val = df_melt[df_melt["country"] == country].year.tolist()
        y_val = df_melt[df_melt["country"] == country].percentrural.tolist()
        data.append((country, x_val, y_val))
    del df, new_df, df_melt, cols

    return data, df_new


if __name__ == "__main__":
    _, df = prepared_data()
    print(df.head(3))
