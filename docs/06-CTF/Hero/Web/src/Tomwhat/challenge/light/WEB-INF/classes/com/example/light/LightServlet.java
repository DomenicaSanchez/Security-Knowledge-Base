package com.example.light;

import java.io.IOException;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.*;

public class LightServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {

        resp.setContentType("text/html;charset=UTF-8");
        HttpSession session = req.getSession();
        String username = (String) session.getAttribute("username");
        String error = (String) req.getAttribute("error");

        StringBuilder html = new StringBuilder();
        html.append("<html><body><h1>Light Side</h1>");

        if (error != null) {
            html.append("<p style='color:red;'>").append(error).append("</p>");
        }

        html.append("<form method='post'>");
        html.append("<input name='username' />");
        html.append("<button type='submit'>Join</button>");
        html.append("</form>");

        if (username != null) {
            html.append("<p>You are on the good side Lord ").append(username).append("</p>");
            html.append("<form action='/dark/' method='get'><button>Go dark</button></form>");
        }

        html.append("</body></html>");
        resp.getWriter().write(html.toString());
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp)
            throws ServletException, IOException {
        String username = req.getParameter("username");
        if ("darth_sidious".equalsIgnoreCase(username)) {
            req.setAttribute("error", "Forbidden username.");
            doGet(req, resp);
            return;
        }
        req.getSession().setAttribute("username", username);
        resp.sendRedirect(req.getContextPath() + "/");
    }
}
