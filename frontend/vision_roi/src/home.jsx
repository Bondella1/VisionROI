import './home.css'
const Home = ({ onLoginClick }) => {

  return (
    <div className="home">
      <header className="home">
        <h1>Vision ROI</h1>
        <p className="tagline">Turn Insights into Profits with Data-Driven Decisions</p>
      </header>

      <section className="home-intro">
        <h2>What is Vision ROI?</h2>
        <p> 
          Vision ROI is a powerful tool that analyzes company project success, offering actionable insights, revenue forecasts, and return-on-investment (ROI) calculations. Make informed decisions and optimize your business strategy.
        </p>
      </section>

      <section className="home-features">
      <h2>Why Choose Vision ROI?</h2>
      <ul>
        <li><strong>Data-Driven Decisions:</strong> Leverage company success data for smarter investments.</li>
        <li><strong>Revenue & ROI Calculation:</strong> Get real-time insights on profitability.</li>
        <li><strong>Impact Analysis:</strong> Understand how your project affects users & employees.</li>
        <li><strong>Project Recommendations:</strong> Get AI-backed suggestions to maximize success.</li>
      </ul>
      </section>

      <section className="home-cta">
        <p>Start optimizing your business today with Vision ROI!</p>
        <button className="cta-button" onClick={onLoginClick}>Get Started</button>
      </section>
    </div>
  );
};
  
export default Home;