using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class Player_Movement : MonoBehaviour
{
    [SerializeField] Projectile bolt;
    public static int curLevel = 1;
    public int playerSpeed = 10;
    private bool facingRight = false;
    public int playerJumpPower = 1250;
    private float moveX; //variable used to hold player inputs
    public bool isGrounded;
    public bool canAttack = false;
    public int curHealth;
    public int maxHealth = 5;
    

    Animator anim;
    SpriteRenderer sr;
    Transform t;
    Rigidbody2D rgb2D;

    // Use this for initialization
    void Start()
    {
        curHealth = maxHealth;
}
        // Update is called once per frame
    void Update()
    {
        t = GetComponent<Transform>();
        sr = GetComponent<SpriteRenderer>();
        anim = GetComponent<Animator>();
        rgb2D = GetComponent<Rigidbody2D>();
        PlayerMovement();
    }

    void PlayerMovement() { 
        //Controls
        moveX = Input.GetAxis("Horizontal"); // takes player input
        if (Input.GetButtonDown("Jump") && (isGrounded == true))
        {
            Jump();
        }
        if (moveX != 0)
        {
           anim.SetBool("IsRunning", true);
        } else
        {
           anim.SetBool("IsRunning", false);
        }

        //Animations
        
        //Player Direction
        if (moveX < 0.0f)
        {
           sr.flipX = true;
        }else 
        {
           sr.flipX = false;
        }
        //Physics
        rgb2D.velocity = new Vector2(moveX * playerSpeed, rgb2D.velocity.y); 

        if (curHealth > maxHealth)
        {
            curHealth = maxHealth;
        }
        if (curHealth <= 0)
        {
            Die();
        }
    }
    void Jump()
    {
        //Jumping Code
        rgb2D.AddForce(Vector2.up * playerJumpPower);
        isGrounded = false;

    }
    void Die()
    {
        SceneManager.LoadScene("Einhert_Start");
    }


    void OnCollisionEnter2D (Collision2D col) //Will check if player hits the ground
    {
        Debug.Log("Player has collided with " + col.collider.name); //col.collider.name calls the name of the sprite/texture it collides with
        if (col.gameObject.tag == "ground")
        {
            isGrounded = true;
        } //this limits our jumps to one. resume basic tutorial at part 5 20 minutes in
    }

    void LaunhProjectile()
    {
        Projectile pro = Instantiate(bolt, transform.position, Quaternion.identity);
        pro.FireLeft(sr.flipX);
    }
}
