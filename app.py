import streamlit as st
from PIL import Image
import pandas as pd
import requests
from io import BytesIO
import google.generativeai as genai

# Set page config
st.set_page_config(
    page_title="Smit Patel - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load your profile picture (replace with your actual image URL)
profile_pic_url = "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80"
response = requests.get(profile_pic_url)
profile_pic = Image.open(BytesIO(response.content))

# Initialize Gemini (will only load if used in AI Chat section)
if "gemini_model" not in st.session_state:
    st.session_state.gemini_model = None

# CSS for styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 2])
with col1:
    st.image(profile_pic, width=200)
    
with col2:
    st.title("SMIT PATEL")
    st.subheader("Mechanical Engineer | Data Analyst | Cloud Enthusiast")
    st.write("""
    Passionate about leveraging technology to solve complex problems. 
    Skilled in Data Analytics, Cloud Computing, and Web Development with 
    hands-on experience in manufacturing optimization and IoT solutions.
    """)
    
    # Social links
    st.write("""
    📧 Email: smit.patel@example.com  
    🔗 LinkedIn: [linkedin.com/in/smitpatel](https://www.linkedin.com)  
    🐱 GitHub: [github.com/smitpatel](https://www.github.com)  
    📞 Phone: +91 XXXXX XXXXX
    """)

# Navigation
st.markdown("---")
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", 
                         ["About", "Skills", "Projects", "Experience", "Education", "Certifications", "AI Chat"])

# About Section
if section == "About":
    st.header("About Me")
    st.write("""
    I'm a Mechanical Engineering graduate with a minor in Computer Science, passionate about the intersection 
    of engineering and technology. My academic journey at Nirma University has equipped me with strong 
    problem-solving skills and technical expertise across multiple domains.
    
    With hands-on experience in manufacturing optimization, data analytics, and cloud computing, 
    I thrive in environments that require both technical and analytical thinking. My internships 
    at Suzlon Energy and Kabra Extrusion Technik have given me practical insights into industrial 
    processes and data-driven decision making.
    
    When I'm not coding or analyzing data, you can find me exploring new technologies, contributing 
    to open-source projects, or working on IoT-based solutions.
    """)
    
    # Skills preview
    st.subheader("Key Competencies")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        - Data Analytics
        - Cloud Computing
        - Process Optimization
        """)
    with col2:
        st.markdown("""
        - Web Development
        - IoT Solutions
        - Manufacturing Tech
        """)
    with col3:
        st.markdown("""
        - Problem Solving
        - Team Leadership
        - Agile Methodologies
        """)

# Skills Section
elif section == "Skills":
    st.header("Technical Skills")
    
    # Languages
    st.subheader("Programming Languages")
    lang_data = {
        "Language": ["C", "Python", "Java", "JavaScript", "HTML/CSS", "SQL"],
        "Proficiency": [85, 90, 75, 80, 85, 85]
    }
    lang_df = pd.DataFrame(lang_data)
    st.dataframe(lang_df.set_index("Language"), use_container_width=True)
    
    # Tools & Technologies
    st.subheader("Tools & Technologies")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - **PowerBI**: Advanced
        - **MySQL**: Advanced
        - **Solidworks**: Intermediate
        - **GitHub**: Advanced
        """)
    with col2:
        st.markdown("""
        - **OracleDB**: Intermediate
        - **MongoDB**: Intermediate
        - **GenerativeAI**: Beginner
        - **AWS/Oracle Cloud**: Intermediate
        """)
    
    # Areas of Interest
    st.subheader("Areas of Interest")
    st.markdown("""
    - Data Analytics
    - Cloud Computing
    - Web Development
    - Internet of Things (IoT)
    - Manufacturing Optimization
    - Artificial Intelligence
    """)
    
    # Soft Skills
    st.subheader("Soft Skills")
    st.markdown("""
    - Problem Solving
    - Adaptability
    - Teamwork
    - Leadership
    - Communication
    - Time Management
    """)

# Projects Section
elif section == "Projects":
    st.header("Projects")
    
    # Project 1
    with st.expander("Python GUI for Pressure Vessel Components", expanded=True):
        st.markdown("""
        **Description**: Developed a responsive frontend and backend application for pressure vessel component calculations.
        
        **Technologies Used**: Python, Django, MySQL, JSON
        
        **Key Achievements**:
        - Automated complex calculations, improving efficiency by 30%
        - Reduced manual errors in pressure vessel design
        - Implemented responsive UI for better user experience
        
        **Relevant Links**:
        - [GitHub Repository](https://github.com/smitpatel/pressure-vessel-gui)
        - [Live Demo](https://pressure-vessel-demo.example.com)
        """)
    
    # Project 2
    with st.expander("Supply Chain Management of Engineering Mall Link"):
        st.markdown("""
        **Description**: Developed a Maintenance, Repair, and Operations (MRO) based delivery model hosted on Amazon SmartBiz.
        
        **Technologies Used**: Power BI, Lean Six Sigma, Amazon SmartBiz
        
        **Key Achievements**:
        - Reduced excess inventory by 15% using Lean & Six Sigma principles
        - Boosted sourcing speed by 20%
        - Developed Power BI dashboards for real-time tracking
        - Improved stock availability through demand forecasting
        
        **Relevant Links**:
        - [Project Documentation](https://drive.google.com/engineering-mall-docs)
        - [Power BI Dashboard](https://app.powerbi.com/engineering-mall)
        """)
    
    # Project 3
    with st.expander("Accenture - Data Analytics & Visualization Job Simulation"):
        st.markdown("""
        **Description**: Analyzed large datasets to uncover trends and develop custom visualizations for business insights.
        
        **Technologies Used**: Python (Pandas, NumPy, Matplotlib, Seaborn), Power BI
        
        **Key Achievements**:
        - Analyzed 7 large datasets to identify key trends
        - Developed enhanced social media engagement strategies
        - Applied EDA and statistical analysis for actionable insights
        
        **Relevant Links**:
        - [GitHub Repository](https://github.com/smitpatel/accenture-data-sim)
        - [Certificate of Completion](https://accenture.certificates.example.com/smitpatel)
        """)
    
    # Project 4
    with st.expander("Drowsiness Detection System"):
        st.markdown("""
        **Description**: Built a real-time ML-based system to detect driver drowsiness and improve road safety.
        
        **Technologies Used**: OpenCV, TensorFlow, CNN, IoT
        
        **Key Achievements**:
        - Achieved 90% accuracy in drowsiness detection
        - Trained CNN model for eye movement pattern recognition
        - Integrated IoT-based alert system for immediate notifications
        
        **Relevant Links**:
        - [GitHub Repository](https://github.com/smitpatel/drowsiness-detection)
        - [Research Paper](https://arxiv.org/drowsiness-detection-smitpatel)
        """)

# Experience Section
elif section == "Experience":
    st.header("Professional Experience")
    
    # Suzlon Energy
    with st.expander("Suzlon Energy - Project Intern (Jan-April 2025)", expanded=True):
        st.markdown("""
        **Location**: Daman  
        **Role**: Full BOM upgradation & Throughput time reduction for manufacturing St44 Wind Mill.
        
        **Key Responsibilities & Achievements**:
        - Collected raw data through Time study to identify trends across different shifts
        - Developed new Bill of Material by rectifying actual material consumption
        - Reduced BOM variation by 83% through process optimization
        - Performed Data analysis to identify bottlenecks, reducing Throughout time by 7%
        - Optimized Manpower allocation for improved efficiency
        - Created revised edition of SOP (Structure of Procedure) for various manufacturing stages
        
        **Technologies Used**: Time Study Analysis, Data Analytics, Process Optimization, SOP Development
        """)
    
    # Kabra Extrusion
    with st.expander("Kabra Extrusion Technik Ltd. - Summer Intern (Jun-Jul 2024)"):
        st.markdown("""
        **Location**: Daman  
        **Role**: Manufacturing Department Intern
        
        **Key Responsibilities & Achievements**:
        - Built complete extrusion plants for blown film, drip irrigation, & PVC
        - Oversaw equipment maintenance & quality control for optimal performance
        - Gained hands-on experience in manufacturing processes
        - Assisted in quality assurance procedures
        
        **Technologies Used**: Manufacturing Processes, Equipment Maintenance, Quality Control
        """)

# Education Section
elif section == "Education":
    st.header("Education")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Bachelor of Technology in Mechanical Engineering")
        st.markdown("""
        **Institute**: Institute of Technology Nirma University, Ahmedabad  
        **Duration**: 2021-2025  
        **CGPA**: 7.0/10.0
        
        **Key Coursework**:
        - Advanced Manufacturing Processes
        - Thermodynamics and Heat Transfer
        - Machine Design
        - Industrial Engineering
        - Computer-Aided Design
        """)
    
    with col2:
        st.subheader("Minor Degree in Computer Science")
        st.markdown("""
        **Institute**: Institute of Technology Nirma University, Ahmedabad  
        **Duration**: 2021-2025
        
        **Key Coursework**:
        - Data Structures and Algorithms
        - Database Management Systems
        - Web Technologies
        - Artificial Intelligence
        - Cloud Computing
        """)

# Certifications Section
elif section == "Certifications":
    st.header("Certifications")
    
    # Oracle Certifications
    with st.expander("Oracle Certifications", expanded=True):
        st.markdown("""
        - **Oracle AI Vector Search Certified Professional**  
          [View Certificate](https://oracle.certificates.example.com/ai-vector-search)  
          *Skills Gained*: AI vector search techniques, Oracle AI infrastructure
        
        - **Oracle Cloud Infrastructure 2024 Data Certified Foundation Associate**  
          [View Certificate](https://oracle.certificates.example.com/oci-data)  
          *Skills Gained*: Oracle Cloud data services, database management
        
        - **Oracle Cloud Infrastructure 2024 AI Certified Foundation Associate**  
          [View Certificate](https://oracle.certificates.example.com/oci-ai)  
          *Skills Gained*: AI services on Oracle Cloud, machine learning models
        """)
    
    # Other Certifications
    with st.expander("Other Professional Certifications"):
        st.markdown("""
        - **Google Analytics Certification**  
          [View Certificate](https://analytics.google.com/certificate/smitpatel)  
          *Skills Gained*: Web analytics, data interpretation, KPI tracking
        
        - **Database Management Systems (Infosys)**  
          [View Certificate](https://infosys.certificates.example.com/dbms)  
          *Skills Gained*: SQL, database design, normalization
        
        - **Introduction to Cyber Security (Infosys)**  
          [View Certificate](https://infosys.certificates.example.com/cybersecurity)  
          *Skills Gained*: Security fundamentals, threat analysis
        
        - **Programming Fundamentals using Python (Infosys)**  
          [View Certificate](https://infosys.certificates.example.com/python)  
          *Skills Gained*: Python programming, OOP concepts
        """)

# AI Chat Section (Gemini Version)
elif section == "AI Chat":
    st.header("Ask AI About My Profile")
    st.info("This feature uses Google's Gemini AI to answer questions about my skills, experience, and projects.")
    
    if "gemini_key" not in st.secrets:
        st.warning("Please set up your Gemini API key in Streamlit secrets to use this feature.")
    else:
        # Initialize Gemini model
        if st.session_state.gemini_model is None:
            genai.configure(api_key=st.secrets["gemini_key"])
            st.session_state.gemini_model = genai.GenerativeModel('gemini-pro')
        
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {"role": "assistant", "content": "Hi! I can answer questions about Smit Patel's professional profile. What would you like to know?"}
            ]
        
        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # User input
        if prompt := st.chat_input("Ask about my skills, projects, or experience"):
            # Add user message to history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate context
            context = """
            Smit Patel is a Mechanical Engineer with a minor in Computer Science from Nirma University (2021-25, CGPA 7.0).
            
            Technical Skills:
            - Languages: C, Python, Java, JavaScript, HTML+CSS, SQL
            - Tools: PowerBI, MySQL, Solidworks, GitHub, OracleDB, MongoDB, GenerativeAI
            - Cloud: Oracle Cloud, AWS
            - Interests: Data Analytics, Cloud, Web Development, IoT
            
            Experience:
            1. Suzlon Energy (Jan-Apr 2025):
               - Project Intern for BOM upgradation & throughput time reduction
               - Reduced BOM variation by 83%, throughput time by 7%
               - Developed new SOPs for manufacturing
            
            2. Kabra Extrusion (Jun-Jul 2024):
               - Summer Intern in Manufacturing
               - Built extrusion plants, oversaw maintenance & QC
            
            Projects:
            1. Python GUI for Pressure Vessel:
               - Django, MySQL, JSON
               - 30% efficiency improvement
            
            2. Supply Chain Management:
               - Lean Six Sigma, Power BI
               - 15% inventory reduction
            
            3. Accenture Data Simulation:
               - Python data analysis
               - Power BI visualizations
            
            4. Drowsiness Detection:
               - OpenCV, TensorFlow
               - 90% accuracy
            
            Certifications:
            - Multiple Oracle Cloud/AI certifications
            - Google Analytics
            - Infosys certifications in DBMS, Cybersecurity, Python
            """
            
            try:
                # Generate response using Gemini
                response = st.session_state.gemini_model.generate_content(
                    f"Context about Smit Patel:\n{context}\n\nUser Question: {prompt}\n\n"
                    "Answer concisely in 1-3 sentences focusing only on relevant information from the context:"
                )
                ai_response = response.text
            except Exception as e:
                ai_response = f"Sorry, I encountered an error: {str(e)}"
            
            # Display and store AI response
            with st.chat_message("assistant"):
                st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <p>© 2024 Smit Patel | Built with Streamlit and Gemini AI</p>
    <p>Last updated: June 2024</p>
</div>
""", unsafe_allow_html=True)
