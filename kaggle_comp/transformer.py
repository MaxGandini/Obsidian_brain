import os
from pathlib import Path
import numpy as np 
import torch
import polars as pl

grandparent_dir= Path(__file__).parents[2]

data_path = grandparent_dir / "datasets" / "part-0.parquet"


for i in range(1):
    # Read the parquet file
    df = pl.read_parquet(data_path)
    
    # Drop columns with all null values
    df = df.select([col for col in df.columns if not df[col].is_null().all()])

    # Get the first 'date_id'
    first_date_id = df.select(pl.col('date_id').min()).to_series()[0]

    # Filter rows where 'date_id' equals the first_date_id
    filtered_grouped = df.filter(pl.col('date_id') == first_date_id)

    # Identify all responder columns
    responders = [col for col in df.columns if "responder" in col]

    # Pivot table
    pivot_df = filtered_grouped.pivot(
    values=responders,
    index="time_id",
    on="symbol_id",
    )
    # Replace missing values with 0
    pivot_df = pivot_df.fill_null(0)

    # Display the shape for debugging
    print("Pivoted DataFrame shape:", pivot_df.shape)

    # Example array for verification
    responder_6_columns = [col for col in pivot_df.columns if 'responder_6' in col]
    responder_6_indices = [pivot_df.columns.index(col)-1 for col in responder_6_columns]
    
    # Convert the DataFrame to a numpy array
    result_array = pivot_df.to_numpy()
    
    result_tensor = torch.from_numpy(result_array).float()

    # Display the shape for debugging
    print("Resulting Tensor shape:", result_tensor.shape)

    # Example: Extract specific responder columns
    responder_6_columns = [col for col in pivot_df.columns if 'responder_6' in col]
    responder_6_indices = [pivot_df.columns.index(col) for col in responder_6_columns]
    
    responder_6_data = result_tensor[:, responder_6_indices]
    print(len(responder_6_indices), responder_6_columns, responder_6_data.shape)

from transformers import InformerConfig, InformerModel

configuration = InformerConfig(prediction_length=13)

model = InformerModel(configuration)

#from huggingface_hub import login
#login()

from transformers import TrainingArguments
from transformers import Trainer

training_args = TrainingArguments(
    output_dir="peeker",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=True,
)
train_data = result_tensor[:700]
eval_data = result_tensor[-149:]

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=eval_data,
    data_collator=None
)

trainer.train()
