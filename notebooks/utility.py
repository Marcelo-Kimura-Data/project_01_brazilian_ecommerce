


def configuracao_schema(schema, df)
    for coluna, tipo_esperado in schema.items():
        if "datetime" in tipo_esperado:
            df[coluna] = pd.to_datetime(df[coluna], errors="coerce")
        else:
            df[coluna] = df[coluna].astype(tipo_esperado)
        return df









            