import xml.etree.ElementTree as ET
import pandas as pd


def xml_to_df(path):
    tree = ET.parse(path)
    root = tree.getroot()
    columns = set()
    columns.add('node depth')
    columns = recurse_columns(root, columns)
    df = pd.DataFrame(columns=list(columns))
    df = recurse_node(root, df)
    print(df.head())


def recurse_columns(node, columns: set, depth=0):
    depth += 1
    for child in node:
        if depth > 1:
            columns.add(child.tag)
        _ = recurse_columns(child, columns, depth)
    return columns


def recurse_node(node, df: pd.DataFrame, depth=0):
    depth += 1
    for child in node:
        l = [child.text if child.tag == col else "" for col in df.columns]
        l[-1] = depth

        df.loc[df.shape[0]] = l
        _ = recurse_node(child, df, depth)
    return df


if __name__ == '__main__':
    xml_to_df('plant_catalog.xml')
