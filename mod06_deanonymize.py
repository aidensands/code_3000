import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df:pd.DataFrame, aux_df:pd.DataFrame):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    keys = ['age', 'zip3', 'gender']
    anon_df = anon_df.drop_duplicates(subset=keys, keep=False)
    aux_df = aux_df.drop_duplicates(subset=keys, keep=False)
    merged = anon_df.merge(aux_df, on=keys, how='inner')
    merged = merged.rename(columns={'name':'matched_name'})
    return merged.drop(columns=keys) 


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return len(matches_df) / len(anon_df)
