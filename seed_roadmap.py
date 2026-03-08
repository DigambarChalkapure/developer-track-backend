import json
import os

categories = [
    "Core Java", "Java Collections", "Multithreading", "Java 8",
    "Spring Boot", "Spring Security", "Hibernate", "REST APIs",
    "Microservices", "SQL", "System Design", "React",
    "DevOps", "Docker", "Kubernetes", "AWS", "DSA"
]

topics_data = {
    "Core Java": [
        "Data Types & Variables", "Operators", "Control Flow Statements", 
        "Arrays", "String Handling", "OOP - Classes & Objects", 
        "OOP - Inheritance", "OOP - Polymorphism", "OOP - Encapsulation", 
        "OOP - Abstraction", "Interfaces", "Packages", 
        "Exception Handling Basics", "Custom Exceptions"
    ],
    "Java Collections": [
        "Collection Framework Overview", "ArrayList", "LinkedList", 
        "HashSet & TreeSet", "HashMap & TreeMap", "Iterator & ListIterator", 
        "Comparable & Comparator", "Collections Class Utilities", 
        "Queue Interface", "PriorityQueue"
    ],
    "Multithreading": [
        "Thread Creation", "Thread Lifecycle", "Synchronization", 
        "Volatile Keyword", "Wait & Notify", "Deadlock", 
        "Callable & Future", "Executors Framework", "ThreadLocal", 
        "Concurrent Collections overview"
    ],
    "Java 8": [
        "Lambda Expressions", "Functional Interfaces", "Streams API Filter", 
        "Streams API Map & Reduce", "Optional Class", "Method References", 
        "Default & Static Methods in Interfaces", "Date and Time API", 
        "CompletableFuture basics", "Spliterator"
    ],
    "Spring Boot": [
        "Spring Core & IoC", "Dependency Injection", "Spring Boot Annotations", 
        "Application Properties", "Spring MVC Architecture", "Controllers & Routing", 
        "Service & Repository Layers", "Exception Handling (@ControllerAdvice)", 
        "Spring Boot Actuator", "Profiles"
    ],
    "Spring Security": [
        "Security Architecture", "Authentication Basics", "Authorization & Roles", 
        "JWT Concepts", "Configuring SecurityFilterChain", "UserDetailsService", 
        "Password Encoding", "Method Level Security", "OAuth2 Basics", 
        "CORS & CSRF Filtering"
    ],
    "Hibernate": [
        "JPA vs Hibernate", "Entity Mapping", "Primary Key Generation", 
        "CRUD Operations", "HQL (Hibernate Query Language)", "Criteria API", 
        "One-to-One Mapping", "One-to-Many Mapping", "Many-to-Many Mapping", 
        "Caching (L1 & L2)"
    ],
    "REST APIs": [
        "REST Principles", "HTTP Methods", "Status Codes", 
        "Request & Response Payloads", "Content Negotiation", "Versioning APIs", 
        "Pagination & Filtering", "HATEOAS", "Swagger / OpenAPI Documentation", 
        "API Security Best Practices"
    ],
    "Microservices": [
        "Microservices vs Monolith", "Service Discovery (Eureka)", 
        "API Gateway", "Config Server", "Circuit Breaker Pattern", 
        "Distributed Tracing", "Event-Driven Architecture", "Saga Pattern", 
        "CQRS Basics", "Centralized Logging"
    ],
    "SQL": [
        "Basic SELECTs & Filtering", "JOINs (Inner, Outer, Left, Right)", 
        "Group By & Having", "Subqueries", "Common Table Expressions (CTEs)", 
        "Window Functions", "Indexes", "Transactions & ACID Properties", 
        "Normalization Basics", "Stored Procedures Basics"
    ],
    "System Design": [
        "Client-Server Architecture", "Load Balancing", "Caching Strategies", 
        "Database Sharding & Replication", "CAP Theorem", "Message Queues", 
        "Rate Limiting", "Consistent Hashing", "CDN", "Designing URL Shortener"
    ],
    "React": [
        "JSX & Components", "Props & State", "Component Lifecycle / Hooks Overview", 
        "useState & useEffect", "React Router", "Context API", 
        "Handling Forms", "useMemo & useCallback", "Custom Hooks", 
        "State Management Libraries (Redux/Zustand)"
    ],
    "DevOps": [
        "SDLC & Agile", "CI/CD Pipeline Concepts", "Git Branching Strategies", 
        "Linux Basics & Shell Scripting", "Nginx/Apache Routing", "Monitoring tools (Prometheus/Grafana)", 
        "Log Management (ELK)", "Infrastructure as Code (Terraform)", "Ansible Basics", 
        "Security Scanning Basics"
    ],
    "Docker": [
        "Containers vs VMs", "Docker Architecture", "Writing Dockerfiles", 
        "Docker Images & Registries", "Docker Networking", "Docker Volumes", 
        "Docker Compose", "Multi-Stage Builds", "Dockerizing a Spring Boot App", 
        "Dockerizing a React App"
    ],
    "Kubernetes": [
        "K8s Architecture", "Pods & Nodes", "Deployments & ReplicaSets", 
        "Services (ClusterIP, NodePort, LoadBalancer)", "ConfigMaps & Secrets", 
        "Ingress Controllers", "Persistent Volumes", "StatefulSets", 
        "Helm Charts basics", "K8s Namespaces"
    ],
    "AWS": [
        "IAM (Users, Roles, Policies)", "EC2 Basics", "S3 Storage", 
        "VPC & Subnets", "RDS (Relational Database Service)", "DynamoDB (NoSQL)", 
        "Lambda (Serverless)", "API Gateway", "Elastic Beanstalk", 
        "CloudWatch"
    ],
    "DSA": [
        "Big O Notation", "Arrays & Strings Applications", "Linked Lists (Singly/Doubly)", 
        "Stacks & Queues", "Trees (Binary, BST)", "Graphs (BFS/DFS)", 
        "Sorting Algorithms", "Searching Algorithms", "Dynamic Programming Basics", 
        "Greedy Algorithms"
    ]
}

roadmap = []
topic_id = 1

for category in categories:
    cat_topics = topics_data.get(category, [])
    for t_idx, topic in enumerate(cat_topics):
        roadmap.append({
            "id": topic_id,
            "category": category,
            "topic": category,
            "subtopic": topic,
            "completed": False,   # Will be overridden per-user
            "difficulty": "medium", 
            "estimated_hours": 2,
            "notes": "",
            "last_updated": ""
        })
        topic_id += 1

output_file = os.path.join(os.path.dirname(__file__), 'data', 'roadmap.json')
with open(output_file, 'w') as f:
    json.dump(roadmap, f, indent=4)

print(f"Generated {topic_id - 1} topics in {output_file}")
