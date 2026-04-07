# 📁 1. Model (User.java)

```java
package com.example.demo.model;

import jakarta.persistence.*;

@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String name;
    private String email;

    public User() {}

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    // getters and setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
}
```

---

# 🗄️ 2. Repository (UserRepository.java)

```java
package com.example.demo.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.model.User;

public interface UserRepository extends JpaRepository<User, Integer> {
}
```

---

# 🎮 3. Controller (UserController.java)

```java
package com.example.demo.controller;

import com.example.demo.model.User;
import com.example.demo.repository.UserRepository;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class UserController {

    private final UserRepository repo;

    public UserController(UserRepository repo) {
        this.repo = repo;
    }

    // Home page (form + list)
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("user", new User());
        model.addAttribute("list", repo.findAll());
        return "form";
    }

    // Save (insert/update)
    @PostMapping("/save")
    public String save(@ModelAttribute User user) {
        repo.save(user);
        return "redirect:/";
    }

    // Edit
    @GetMapping("/edit/{id}")
    public String edit(@PathVariable int id, Model model) {
        model.addAttribute("user", repo.findById(id).orElse(new User()));
        model.addAttribute("list", repo.findAll());
        return "form";
    }

    // Delete
    @GetMapping("/delete/{id}")
    public String delete(@PathVariable int id) {
        repo.deleteById(id);
        return "redirect:/";
    }
}
```

---

# 🌐 4. Thymeleaf UI (form.html)

📁 `src/main/resources/templates/form.html`

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>User App</title>
</head>
<body>

<h2>User Form</h2>

<form th:action="@{/save}" th:object="${user}" method="post">

    <input type="hidden" th:field="*{id}">

    Name: <input type="text" th:field="*{name}" /><br><br>
    Email: <input type="email" th:field="*{email}" /><br><br>

    <button type="submit">Save</button>
</form>

<hr>

<h2>Users List</h2>

<table border="1">
<tr>
<th>ID</th><th>Name</th><th>Email</th><th>Action</th>
</tr>

<tr th:each="u : ${list}">
    <td th:text="${u.id}"></td>
    <td th:text="${u.name}"></td>
    <td th:text="${u.email}"></td>
    <td>
        <a th:href="@{/edit/{id}(id=${u.id})}">Edit</a>
        <a th:href="@{/delete/{id}(id=${u.id})}">Delete</a>
    </td>
</tr>

</table>

</body>
</html>
```

---

# ⚙️ 5. application.properties

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/testdb
spring.datasource.username=root
spring.datasource.password=yourpassword

spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true

spring.thymeleaf.cache=false
```

---

# 🛢️ 6. MySQL (Only DB needed)

```sql
CREATE DATABASE testdb;
```

👉 No table needed — JPA creates it automatically

---

# ▶️ Run Steps

1. Start MySQL
2. Create DB `testdb`
3. Run Spring Boot
4. Open:

```
http://localhost:8080/
```

---

# 🔥 What you get

✔ Add user
✔ Update user
✔ Delete user
✔ View users
✔ MySQL connected
✔ JPA (no SQL writing)
✔ Proper MVC (Thymeleaf)

---

If you want, I can compress this into a **1-page exam cheat sheet (super revision mode)** or add **search + validation in 2 lines** 👍



Here is the **final clean file structure** for your Spring Boot + JPA + MySQL + Thymeleaf project 👇

---

# 📁 FINAL FILE STRUCTURE

```
demo/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── example/
│   │   │           └── demo/
│   │   │               ├── DemoApplication.java
│   │   │               │
│   │   │               ├── controller/
│   │   │               │   └── UserController.java
│   │   │               │
│   │   │               ├── model/
│   │   │               │   └── User.java
│   │   │               │
│   │   │               └── repository/
│   │   │                   └── UserRepository.java
│   │   │
│   │   └── resources/
│   │       ├── templates/
│   │       │   └── form.html
│   │       │
│   │       └── application.properties
│
└── target/   (auto-generated)
```

---

# 🧠 Quick Understanding

* **DemoApplication.java** → Main class (runs Spring Boot)
* **controller/** → Handles requests (UserController)
* **model/** → Entity class (User)
* **repository/** → JPA interface (UserRepository)
* **templates/** → Thymeleaf UI (form.html)
* **application.properties** → MySQL config

---

# ⚡ Ultra-Short Memory Trick

👉 Just remember:

```
controller → model → repository → templates → properties
```


Just tell 👍
