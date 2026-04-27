import React, { useState } from 'react';

const EXPERIENCES = [
  {
    icon: '🦅',
    title: 'Sea Eagle Safari',
    description: 'Dawn departure from Portree. Boat-based watch along the Trotternish coast with a ranger naturalist.',
    price: 'From £95 per person',
  },
  {
    icon: '🥾',
    title: 'Quiraing Ridge Walk',
    description: 'Full-day circular across the northern Trotternish escarpment. Suitable for fit walkers with good footwear.',
    price: 'From £65 per person',
  },
  {
    icon: '🚣',
    title: 'Sea Kayak — Loch Coruisk',
    description: 'Paddle into the glacial loch beneath the Cuillin. Half-day guided session, all equipment provided.',
    price: 'From £80 per person',
  },
  {
    icon: '🌿',
    title: 'Foraging & Coast Walk',
    description: 'Learn what is edible along the shoreline. Finish with a fire-cooked meal on the beach.',
    price: 'From £55 per person',
  },
];

const CARD_ACCENTS = ['#7b5ea7', '#c9973a', '#1c3a2a', '#c05a5a'];

function NavBar() {
  return (
    <nav className="navbar">
      <div className="logo">
        Skye<span className="logo-and">&</span>Glen
      </div>
      <ul className="nav-links">
        <li><a href="#experiences">Experiences</a></li>
        <li><a href="#contact">Stay</a></li>
        <li><a href="#contact">Book</a></li>
      </ul>
    </nav>
  );
}

function Hero() {
  return (
    <section className="hero">
      <div className="hero-bg" />
      <div className="hills">
        <div className="hill hill-1" />
        <div className="hill hill-2" />
        <div className="hill hill-3" />
      </div>

      <div className="tech-badge">
        <span className="badge-dot" />
        Served via Cloudflare Workers
      </div>

      <div className="hero-text">
        <p className="hero-tag">Western Isles, Scotland</p>
        <h1 className="hero-title">
          Where the land meets <em>the open sea</em>
        </h1>
        <p className="hero-sub">
          Guided experiences across Skye, the Outer Hebrides and the Highland glens. Small groups. No crowds. Real Scotland.
        </p>
        <div className="hero-buttons">
          <button className="btn-primary">Browse Experiences</button>
          <button className="btn-outline">Read Our Story</button>
        </div>
      </div>

      <div className="perf-bar">
        <span className="perf-item">TTFB <strong>312ms</strong></span>
        <span className="perf-sep">|</span>
        <span className="perf-item">Load time <strong>4.82s</strong> on 15 Mbps</span>
        <span className="perf-sep">|</span>
        <span className="perf-item">Edge node <strong>London, UK</strong></span>
        <span className="perf-sep">|</span>
        <span className="perf-item">Deployment <strong>Cloudflare Workers</strong></span>
      </div>
    </section>
  );
}

function ExperienceCard({ icon, title, description, price, index }) {
  const accent = CARD_ACCENTS[index % CARD_ACCENTS.length];
  return (
    <div className="exp-card" style={{ borderLeft: `3px solid ${accent}` }}>
      <div className="exp-icon">{icon}</div>
      <h3 className="exp-title">{title}</h3>
      <p className="exp-desc">{description}</p>
      <p className="exp-price">{price}</p>
    </div>
  );
}

function Experiences() {
  return (
    <section className="section" id="experiences">
      <p className="section-label">What we offer</p>
      <h2 className="section-title">Slow down. Go further.</h2>
      <p className="body-text">
        We have been running small-group tours across Scotland's western coast since 2011. Every experience is guided by someone who grew up here — someone who knows which single-track roads lead somewhere worth going.
      </p>
      <div className="exp-grid">
        {EXPERIENCES.map((exp, i) => (
          <ExperienceCard key={exp.title} index={i} {...exp} />
        ))}
      </div>
    </section>
  );
}

function Quote() {
  return (
    <section className="quote-section">
      <blockquote className="quote">
        "Three seconds waiting for a page to load loses more than half of rural visitors. Edge computing cuts that wait by a third — and for a small tourism business, that is the difference between a booking and a back button."
      </blockquote>
      <p className="quote-attr">— Research finding, MSc Project 2026</p>
    </section>
  );
}

function Contact() {
  const [form, setForm] = useState({ name: '', email: '', message: '' });
  const [sent, setSent] = useState(false);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    setSent(true);
  }

  return (
    <section className="contact-section section" id="contact">
      <div className="contact-info">
        <p className="section-label">Get in touch</p>
        <h2 className="contact-title">Plan your visit</h2>
        <p><strong>Skye & Glen Tours</strong></p>
        <p>
          Isle of Skye<br />
          IV51 9EE, Scotland
        </p>
        <p className="contact-details">
          hello@skyeandglen.scot<br />
          +44 1478 000 000
        </p>
        <p className="demo-notice">
          This is a demonstration website built for an MSc research project on web performance in rural Scotland. No real bookings are taken and no personal data is stored.
        </p>
      </div>

      <div className="contact-form">
        {sent ? (
          <div className="form-success">
            <p>Thank you — we will be in touch soon.</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              name="name"
              placeholder="Your name"
              value={form.name}
              onChange={handleChange}
              required
            />
            <input
              type="email"
              name="email"
              placeholder="Email address"
              value={form.email}
              onChange={handleChange}
              required
            />
            <textarea
              name="message"
              placeholder="Tell us what you are interested in..."
              value={form.message}
              onChange={handleChange}
              rows={5}
            />
            <button type="submit" className="submit-btn">
              Send Enquiry
            </button>
          </form>
        )}
      </div>
    </section>
  );
}

function Footer() {
  return (
    <footer className="footer">
      <span className="footer-logo">Skye & Glen</span>
      <span className="footer-note">
        Demo site — MSc Web Performance Research 2026 | UWS B01767356
      </span>
    </footer>
  );
}

export default function App() {
  return (
    <div className="site">
      <NavBar />
      <Hero />
      <Experiences />
      <Quote />
      <Contact />
      <Footer />
    </div>
  );
}
