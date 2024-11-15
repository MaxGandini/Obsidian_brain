Most of these notes will be based on 'Rust by example'.

It was designed to address issues often seen in languages like C and C++ (especially around memory safety) while also providing high-level abstractions similar to languages like Python or JavaScript:

## Key Features

- #### Memory Safety without Garbage Collection
	  Rust uses an **ownership model** that enforces memory safety at compile time. This model avoids needing a garbage collector and ensures no null pointer dereferences or data races.

- #### Ownership and Borrowing
	  Each value has a single **owner**, and only one mutable or multiple immutable references are allowed at a time.
	  The Rust compiler enforces this model at compile time, preventing data races.

```rust
  fn main() {
      let s = String::from("hello"); // `s` owns the string
      let r = &s;                     // `r` is an immutable reference to `s`
      println!("{}", r);              // `r` is used safely
  }
```

