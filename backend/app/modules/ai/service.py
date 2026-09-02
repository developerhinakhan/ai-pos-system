from groq import Groq
from sqlalchemy.orm import Session
from app.core.config import settings
from app.modules.products.model import Product
from app.modules.sales.model import Sale
from app.modules.sales.sale_item_model import SaleItem

client = Groq(api_key=settings.GROQ_API_KEY)


class AIService:

    def get_low_stock_analysis(self, db: Session):
        # Get low stock products
        products = db.query(Product).filter(
            Product.stock_quantity <= Product.low_stock_alert
        ).all()

        if not products:
            return {"message": "All products are well stocked!"}

        # Prepare data for AI
        product_data = []
        for p in products:
            product_data.append(
                f"Product: {p.name}, "
                f"Stock: {p.stock_quantity}, "
                f"Alert Level: {p.low_stock_alert}"
            )

        prompt = f"""
        You are a POS system assistant.
        These products have low stock:
        
        {chr(10).join(product_data)}
        
        Provide:
        1. Which products need urgent restocking
        2. Priority order for restocking
        3. Simple recommendations
        
        Keep response short and practical.
        """

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "low_stock_products": [p.name for p in products],
            "ai_analysis": response.choices[0].message.content
        }

    def get_sales_insights(self, db: Session):
        # Get recent sales
        sales = db.query(Sale).order_by(Sale.created_at.desc()).limit(50).all()

        if not sales:
            return {"message": "No sales data available yet"}

        # Prepare data
        total_revenue = sum(s.final_amount for s in sales)
        total_sales = len(sales)
        avg_sale = total_revenue / total_sales if total_sales > 0 else 0

        prompt = f"""
        You are a POS system analyst.
        Here is the sales data:
        
        Total Sales: {total_sales}
        Total Revenue: {total_revenue}
        Average Sale Amount: {avg_sale:.2f}
        
        Provide:
        1. Sales performance summary
        2. Key insights
        3. Simple recommendations to improve revenue
        
        Keep response short and practical.
        """

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "total_sales": total_sales,
            "total_revenue": total_revenue,
            "average_sale": round(avg_sale, 2),
            "ai_insights": response.choices[0].message.content
        }

    def get_recommendations(self, db: Session):
        # Get products and sales data
        products = db.query(Product).all()
        sales = db.query(Sale).order_by(Sale.created_at.desc()).limit(20).all()

        if not products:
            return {"message": "No products available"}

        product_info = []
        for p in products:
            product_info.append(
                f"Product: {p.name}, "
                f"Price: {p.price}, "
                f"Stock: {p.stock_quantity}, "
                f"Active: {p.is_active}"
            )

        prompt = f"""
        You are a smart POS system advisor.
        
        Products: {chr(10).join(product_info)}
        Recent sales count: {len(sales)}
        
        Provide 3-5 specific business recommendations:
        1. Inventory management
        2. Pricing strategy
        3. Stock optimization
        
        Keep it practical and actionable.
        """

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "total_products": len(products),
            "ai_recommendations": response.choices[0].message.content
        }


ai_service = AIService()