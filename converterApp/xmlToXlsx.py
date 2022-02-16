import xml.etree.ElementTree as ET
import pandas as pd


def xml_to_df(path):
    tree = ET.parse(path)
    root = tree.getroot()
    columns = set()
    columns.add('node depth')
    columns.add('node type')
    columns = recurse_columns(root, columns)
    df = pd.DataFrame(columns=list(columns))
    df = recurse_node(root, {col: "" if col != 'node depth' else 1 for col in df.columns}, df)
    df.drop(columns='node depth', inplace=True)
    df.to_csv('output.csv', index=False)


def recurse_columns(node, columns: set, depth=0):
    depth += 1
    for child in node:
        if depth > 1:
            columns.add(child.tag)
        _ = recurse_columns(child, columns, depth)
    return columns


def recurse_node(node, temp_dict: dict, df: pd.DataFrame, depth=0):
    depth += 1
    print(depth, temp_dict['node depth'], node.tag, node.text)
    if depth < temp_dict['node depth']:
        print(df.shape[0])
        df.loc[df.shape[0]] = temp_dict
        for col in temp_dict.keys():
            temp_dict[col] = "" if 'node depth' != col else depth
        temp_dict['node depth'] = depth
        temp_dict['node type'] = node.tag
    for child in node:
        temp_dict[child.tag] = child.text
        temp_dict['node depth'] = depth + 1 if depth + 1 > temp_dict['node depth'] else temp_dict['node depth']
        _ = recurse_node(child, temp_dict, df, depth)
    return df


if __name__ == '__main__':
    xml_to_df('plant_catalog.xml')
