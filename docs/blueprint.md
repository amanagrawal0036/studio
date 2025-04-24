# **App Name**: WicketWise

## Core Features:

- User Authentication: Implement a login page and sign-up page to create a personalized user experience.
- Main Dashboard: Design a main dashboard with a navigation pane and a central body to display various IPL data insights.
- Generate Summary: Use an LLM to generate factual statistical summaries about a player or team based on user prompts. Save the query and the output in the user history. Use a tool to determine when a disclaimer is required, and what its language should be.

## Style Guidelines:

- Primary color: Deep blues for a professional and sophisticated look.
- Secondary colors: Crisp whites and subtle grays for a clean and modern aesthetic.
- Accent: Teal (#008080) for buttons, highlights, and interactive elements to add a touch of vibrancy.
- Clean sans-serif fonts (e.g., Inter, Roboto, or Poppins) for readability and a modern feel.
- Intuitive and professional icons for easy navigation and feature recognition.
- Clean and spacious layout with ample whitespace to improve readability and reduce visual clutter.

## Original User Request:
Here is the **complete and updated UI Design Prompt for WicketWise v2.1**, incorporating all your requested changes:

---

# 🎨 **UI Design Prompt: WicketWise – Personalized AI IPL Data Insights Agent**

**Version:** 2.1  
**Date:** 2025-04-25

---

## **1. Project Overview**

- **Application Name:** WicketWise  
- **Goal:** Design a sophisticated, intuitive, and visually engaging user interface for a personalized AI-powered agent delivering in-depth IPL data insights.  
- **Core Functionality:** WicketWise leverages LLM-based responses to generate personalized IPL analytics. Key features include player/team summaries, head-to-head comparisons, factual query answering, and "what-if" scenario analysis.  
- **Target Audience:** IPL fans, fantasy league players, data enthusiasts, and analysts.  
- **Key Differentiator:** Logged-in users get a personalized experience — including saved insights, query history, and profile management.  
- **Tech Stack:** Gradio frontend; design must align with Gradio components while achieving a polished, modern aesthetic.  
- **Output Types:** Textual summaries, structured tables, interactive comparisons, and chat-style Q&A interfaces.

---

## **2. UI/UX Philosophy & Goals**

- **Modern Aesthetic:** Clean layout, ample whitespace, readable typography (modern sans-serif), and intuitive iconography. Support for dark/light themes is optional.  
- **Personalization First:** Logged-in users should feel ownership of the app. Personal touches like greetings and saved history support this.  
- **Smooth Navigation:** Logical, frictionless transitions between login, dashboard, and core features.  
- **Clear Data Presentation:** Use hierarchy and layout to make complex data readable and digestible.  
- **Responsive Experience:** Quick interactions, loading feedback, and mobile-responsive design (within Gradio’s constraints).  
- **Transparency:** Clearly label factual vs. hypothetical content. Disclaimers are essential for AI-generated outputs.

---

## **3. User Authentication: Login & Sign-Up**

### **Login Experience (First Page)**

- Login window appears by default when app starts.
- **Background:** Stylized, semi-blurred cricket action image or IPL-themed visualization.
- **Centered Login Box:** Clean, minimalist input fields:
  - Email/Username  
  - Password  
  - `Login` button  
  - Link: “Don’t have an account? Sign Up”

### **Sign-Up View (Toggle or Separate Screen)**

- Input fields: Full Name, Email/Username, Password, Confirm Password
- `Sign Up` button
- Link: “Already have an account? Login”
- After successful sign-up, redirect to the **Login Page**.

---

## **4. Post-Login Experience: Main Dashboard**

### **Layout Overview**

#### **Left Column: Navigation Pane**

- **Top:**  
  - App title/logo (`WicketWise`)
  
- **Primary Navigation Buttons (stacked vertically):**
  - `📁 Past Insights`
  - `📜 Past Queries`
  - `📊 Generate Summary`
  - `⚔️ Head-to-Head Analyzer`
  - `❓ Query Answering`
  - `🧠 What-If Scenarios`

- **Bottom Section:**
  - `📞 Contact Us`
  - `ℹ️ About Us`

> 🟩 Clicking **any** of these buttons loads the relevant content in the **main dashboard body area**.

- **Main Body**
  - Before any feature is selected:
    - Large center-aligned greeting:  
      > _“Hi {username}!”_  
      > _“Welcome to WicketWise – your personal IPL data assistant.”_
    - Below greeting: **Four horizontally aligned buttons** for:
      - Generate Summary
      - Head-to-Head
      - Query Answering
      - What-If Scenarios
    - Clicking a button activates the respective feature tab.

- **Top-Right Profile Icon**
  - Dropdown menu when clicked:
    - View/Edit Profile (name, email)
    - Save changes
    - Logout

---

## **5. Feature-Specific UI Design Requirements**

### 🧩 Common Behavior

- **Feature Name Heading:** Each feature tab begins with a prominent, styled heading (e.g., “📊 Generate Summary”).
- **Loading State Feedback:** Button disables + visible loader on all async actions.
- **Save History:** All interactions should be stored (query + output) for user’s personal dashboard.

---

### 📊 **(Tab 1) Generate Summary**

- **Purpose:** Generate factual statistical summaries about a **player** or **team**.
- **UI Layout:**
  - Prompt Input (`gr.Textbox`, multiline).
  - `Generate Summary` button.
  - Below that, display returned **string output** from the backend (`gr.Markdown` or styled `gr.Textbox`).
  - A subtle `Save Summary` button.
- **Backend:** Calls a function with the query, returns a string. Save query and output to user history.

---

### ⚔️ **(Tab 2) Head-to-Head Analyser**

- **Purpose:** Compare performance between two players or teams.
- **UI Layout:**
  - Selector: “Compare by:” → `Player vs Player` or `Team vs Team`
  - After selection:
    - Two dropdowns appear: `Entity 1` and `Entity 2`
    - `Compare Entities` button
  - **Output:** Two visually distinct “Stat Cards” showing results from backend dictionaries.
    - Highlight better-performing metrics.
    - Include `Save Comparison` button.

---

### 💬 **(Tab 3) Query Answering**

- **Purpose:** Answer IPL factual queries from users in chat style.
- **UI Layout:**
  - Vertical, scrollable **chat window** (query-response-query-response).
  - Bottom:  
    - Input textbox  
    - `Ask WicketWise` button  
- **Backend:** Calls LLM for answer; stores question/response in query history.

---

### 🤔 **(Tab 4) What-If Scenarios**

- **Purpose:** Explore hypothetical scenarios using past trends and AI reasoning.
- **UI Layout:**
  - Chat-style layout, same as Tab 3.
  - Each LLM response includes a **disclaimer box**:
    > _“This is a hypothetical analysis based on past data and trends. It is not a prediction or guarantee of actual outcomes.”_
  - Allow user to `Save Scenario`.

---

## **6. General UI Styling Notes**

- **Typography:** Clean sans-serif (e.g., Inter, Roboto, or Poppins).
- **Color Palette:** Modern, professional — mix of deep blues, crisp whites, subtle grays. Use accent color (e.g., orange or teal) for buttons and highlights.
- **Button Design:** Rounded, shadowed with hover effects.
- **Component Customization:** Gradio components styled with consistent padding, border-radius, and color schemes.
- **Error Handling:** Friendly error messages (e.g., “Could not find player X”, “Invalid credentials”, “Please try again”).

---

## **7. Deliverables**

- High-fidelity mockups for:
  - Login Page (Login + Sign-Up)
  - Main Dashboard Layout (with welcome screen and navigation pane)
  - Each of the four Feature Tabs (input + output views)
  - User Profile Dropdown & Edit View
  - Contact Us and About Us pages
  - Past Insights and Query History views

- **Style Guide:**
  - Color palette
  - Typography
  - Icon style
  - Button/input field styles

- Notes on:
  - Loading and feedback behaviors
  - Data saving patterns (query history, saved insights)
  - Component interactions within Gradio limitations

---

This is the **complete UI design prompt** for **WicketWise v2.1**. Let me know if you'd like to adjust anything or need further details!
  