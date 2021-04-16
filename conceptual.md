### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
   Ans-  RESTful routing is a routing process that provides mapping from HTTP verbs (get, post, put, delete, patch) to controller CRUD actions (create, read, update, delete). Instead of relying solely on the URL to indicate what site to visit, a RESTful route depends on the HTTP verb and the URL. 

- What is a resource?
   Ans- A resource is a representation of what the website's URL returns. It can be a file, JSON, or information. Once the resource is grabbed, the developer can decide what to do with it.The fundamental concept in any RESTful API is the resource. A resource is an object with a type, associated data, relationships to other resources, and a set of methods that operate on it. It is similar to an object instance in an object-oriented programming language, with the important difference that only a few standard methods are defined for the resource (corresponding to the standard HTTP GET, POST, PUT and DELETE methods), while an object instance typically has many methods.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    Ans- There is no reason to use render or redirect because building a JSON API passes the information from the route to a JSON dictionary in postgrSQL via POST.

- What does idempotent mean? Which HTTP verbs are idempotent?
    Ans- Idempotent means that the result is the same no matter how many times it is requested. However, the data requested CAN be changed. GET, PUT/PATCH, and DELETE are idempotent because the state of the server will always be the same after the HTTP verb occurs.

- What is the difference between PUT and PATCH?
    Ans- PUT updates the entire server while PATCH updates a small part of it.

- What is one way encryption?
    Ans- One way encryption is when only the user who created the account has access to the password itself non-reversibly. That way a company doesn't store the exact password in its database. However, a company can verify the password as the same input must always have the same output.

- What is the purpose of a `salt` when hashing a password?
    Ans- Adding a 'salt' when cryptographically hashing a password gives a user a unique starting sequence that unpredictably changes the output. Salt can be used by a company to look up a password in its database. But because the hashed password is different every time, there is no way of accessing what the hashed password actually translates to.

- What is the purpose of the Bcrypt module?
    Ans- Bcrypt is a way to cryptographically hash a password. It is intentionally designed to be slow so that it makes it tougher to hack. One tool utilized in Bcrypt is to designate a work factor, how many rounds of encryption you want.

- What is the difference between authorization and authentication?
    Ans- Authentication is the process of verification that an individual, entity or website is who it claims to be. One use of this is to use User.authenticate to see if a user is stored in session. Authorization is checking to see if something (ie a user) has "powers" or access to certain features.
