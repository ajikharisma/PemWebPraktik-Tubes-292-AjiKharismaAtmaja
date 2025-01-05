from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from . import db
from .models import User
from .forms import RegistrationForm, LoginForm, EditUserForm
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

main_bp = Blueprint('main', __name__)

# Route Home
@main_bp.route('/')
def home():
    return render_template('home.html')

# Route Register (Menambah Pengguna)
@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form is valid")  # Debugging: Memastikan validasi form berhasil
        user = User(
            username=form.username.data,
            email=form.email.data,
            role='user'  # Pastikan role-nya adalah 'user'
        )
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('main.login'))
        except Exception as e:
            db.session.rollback()
            print(f"Error saat menyimpan ke database: {str(e)}")  # Debugging: Melihat error saat menyimpan
            if '1062' in str(e):  # Menangkap error duplikasi berdasarkan kode error MySQL (1062)
                flash('Data yang Anda inputkan sudah ada dalam database.', 'danger')
            else:
                flash(f'Terjadi kesalahan: {str(e)}', 'danger')
    else:
        print("Form errors:", form.errors)  # Debugging: Melihat error validasi jika form gagal

    return render_template('register.html', form=form)

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            flash('Login berhasil.', 'success')
            return redirect(url_for('main.dashboard'))
        flash('Username atau password salah.', 'danger')
    return render_template('login.html', form=form)

@main_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Silakan login terlebih dahulu.', 'warning')
        return redirect(url_for('main.login'))

    user_id = session.get('user_id')
    user_role = session.get('role')

    # Jika admin, tampilkan semua pengguna
    if user_role == 'user':
        users = User.query.all()
    else:
        # Jika user biasa, hanya tampilkan data pengguna sendiri
        users = User.query.filter_by(id=user_id).all()

    return render_template('dashboard.html', users=users, role=user_role)


# Edit User
@main_bp.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user = User.query.get_or_404(user_id)
    form = EditUserForm(obj=user)  # Mengisi form dengan data dari database

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        
        # Update password hanya jika ada input baru
        if form.password.data:
            user.set_password(form.password.data)

        try:
            db.session.commit()
            flash('Pengguna berhasil diperbarui!', 'success')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Terjadi kesalahan: {str(e)}', 'danger')

    return render_template('edit_user.html', form=form)

# Delete User
@main_bp.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    user = User.query.get_or_404(user_id)

    try:
        db.session.delete(user)
        db.session.commit()
        flash('Pengguna berhasil dihapus!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Terjadi kesalahan: {str(e)}', 'danger')

    return redirect(url_for('main.dashboard'))  # Redirect ke dashboard


# Add User
@main_bp.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if not username or not email or not password:
            flash('Semua kolom harus diisi!', 'danger')
            return redirect(url_for('main.add_user'))
        
        # Membuat user baru dan hash password menggunakan set_password
        new_user = User(username=username, email=email)
        new_user.set_password(password)  # Set password setelah di-hash
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Pengguna berhasil ditambahkan!', 'success')
            return redirect(url_for('main.dashboard'))  # Redirect ke dashboard
        except Exception as e:
            db.session.rollback()
            flash(f'Terjadi kesalahan: {str(e)}', 'danger')
    
    return render_template('add_user.html')

# Logout Route
@main_bp.route('/logout')
def logout():
    session.clear()
    flash('Anda berhasil logout.', 'success')
    return redirect(url_for('main.login'))