import streamlit as st

def render(data):
    st.markdown("## Key Insights and Recommendations")
    col1, col2=st.columns(2)
    
    with col1:
        st.markdown("### Summary of Findings")
        st.markdown("""
        **Salary Expectations**
        - Average desired salary: €40,000-45,000 annually
        - Significant variation by role and experience level
        - Gap between minimum acceptable and desired compensation
        
        **Critical Success Factors**
        - Remote work options: mentioned by 70%+ of respondents
        - Technology autonomy: ability to choose tools and frameworks
        - Mission alignment: serving public interest as key motivator
        - Contract stability: strong preference for permanent positions
        
        **Sector Preferences**
        - Education and healthcare sectors show highest appeal
        - Environmental and digital transformation initiatives attract interest
        - Traditional administrative roles have lower appeal
        """)
        st.info("""
        **Summary:** 

        The research reveals that digital workers in the public sector expect salaries between 
        €40,000 and €45,000 annually, though this varies based on role and experience. Beyond pay, 
        remote work is crucial, over 70% of respondents prioritize it, alongside the ability to choose 
        their own tools and technologies. Workers are also motivated by meaningful work, particularly 
        jobs that serve the public interest, and strongly prefer permanent contracts over temporary positions. 
        When it comes to sectors, education and healthcare are most attractive to talent, as are roles 
        focused on environmental and digital transformation. Traditional administrative positions, 
        on the other hand, appeal to fewer candidates.
        """)

    with col2:
        st.markdown("### Recommendations")
        st.markdown("""
        **For Policy Makers**
        - Develop flexible remote work policies for digital roles
        - Allow technical autonomy in tool and platform selection
        - Emphasize mission impact in recruitment materials
        
        **For HR and Recruitment**
        - Highlight public service mission in job descriptions
        - Offer competitive compensation packages
        - Streamline hiring processes for technical roles
        - Create clear career progression paths
        
        **For Management**
        - Support modern development practices and tools
        - Enable cross-functional collaboration
        - Invest in continuous learning and development
        - Build communities of practice across agencies
        """)
        st.info("""
        **Summary:** 

        To improve recruitment and retention of digital workers in the public sector, policy makers should 
        create flexible remote work policies and let technical teams choose their own tools and technologies. 
        They should also highlight the importance of public service in their messaging. HR and recruitment 
        teams can help by talking about the meaningful impact of the work in job postings, offering fair 
        salaries that match the market, making hiring processes faster for technical positions, and showing 
        employees clear ways to advance their careers. Finally, managers should support modern ways of working, 
        encourage teams from different departments to work together, give employees opportunities to learn and grow, 
        and create spaces where professionals across different government agencies can share knowledge and experiences.
        """)

    st.success("""
    **Bottom Line**: To compete for digital talent, the public sector must offer competitive 
    compensation, modern work practices, meaningful missions, and professional autonomy. 
    These factors are non-negotiable for experienced tech professionals.
    """)

    st.markdown("### Next Steps")
    st.markdown("""
    1. Conduct detailed salary benchmarking study by role and region
    2. Develop targeted employer branding campaigns
    3. Establish metrics to measure talent attraction and retention
    """)